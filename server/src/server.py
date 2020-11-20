import socket
import mariadb
import sys
import time

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
msgFromServer       = "inserted one metric"
bytesToSend         = str.encode(msgFromServer)

def createUdpSocket():
    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip
    UDPServerSocket.bind((localIP, localPort))
    print("UDP server up and listening")

    return UDPServerSocket

def createMariaDbConnection():
    try:
        return mariadb.connect(user="root",password="password",host="db",port=3306,database="demo1").cursor()
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB platform: {e}")
    return None
    
if __name__ == "__main__":

    udpSocket = createUdpSocket()

    dbCursor = None
    while(dbCursor==None):
        time.sleep(2)
        dbCursor = createMariaDbConnection()

    dbCursor.execute("CREATE TABLE IF NOT EXISTS table_demo (demo_id int auto_increment, demo_hostname varchar(255) not null, created_at timestamp default current_timestamp, primary key(demo_id))")
    print("table table_demo created")
    
    # Listen for incoming datagrams
    while(True):
        bytesAddressPair = udpSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        print("Message from Client:{}".format(message))
        print("Client IP Address:{}".format(address))

        # Sending a reply to client
        udpSocket.sendto(bytesToSend, address)
    