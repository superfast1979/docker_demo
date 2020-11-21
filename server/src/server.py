import socket
import mariadb
import sys
import time

def createUdpSocket():
    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to clientIp and ip
    UDPServerSocket.bind(("0.0.0.0", 20001))
    print("UDP server up and listening")

    return UDPServerSocket

def createMariaDbConnection():
    cursor = None
    while(cursor == None):
        print("connecting to mariadb...")
        time.sleep(2)
        try:
            connection = mariadb.connect(user="root",password="password",host="db",port=3306,database="demo1")
            cursor = connection.cursor()
            return connection, cursor
        except mariadb.Error as e:
            print("Error connecting to MariaDB platform: {}").format(e)
    
if __name__ == "__main__":

    udpSocket = createUdpSocket()
    dbConnection, dbCursor = createMariaDbConnection()

    dbCursor.execute("DROP TABLE IF EXISTS table_demo")
    dbCursor.execute("CREATE TABLE IF NOT EXISTS table_demo (demo_id int auto_increment, demo_client varchar(255) not null, demo_host varchar(255) not null, created_at timestamp default current_timestamp, primary key(demo_id))")
    print("table_demo created")

    serverIpAddress = socket.gethostbyname(socket.gethostname())

    # Listen for incoming datagrams
    while(True):
        message, clientIpPort = udpSocket.recvfrom(1024)
        clientIp = clientIpPort[0]

        print("Message from Client:{}".format(message))
        print("Client IP Address:{}".format(clientIp))

        # Sending a reply to client
        udpSocket.sendto(str.encode("inserted one metric"), clientIpPort)

        dbCursor.execute("INSERT INTO table_demo (demo_client, demo_host) VALUES ('{}', '{}')".format(clientIp, serverIpAddress))
        dbConnection.commit()
        print("record in table_demo inserted")

    dbConnection.close()