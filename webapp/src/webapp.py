from flask import Flask
server = Flask(__name__)
import mariadb
import time

server.dbConnection = None

def createMariaDbConnection():
    cursor = None
    while(cursor == None):
        print("connecting to mariadb...")
        time.sleep(2)
        try:
            connection = mariadb.connect(user="root",password="password",host="db",port=3306,database="demo1")
            return connection
        except mariadb.Error as e:
            print("Error connecting to MariaDB platform: {}").format(e)

@server.route("/")
def hello():
    connection = createMariaDbConnection()
    server.logger.info('%s connection', connection)
    cursor = connection.cursor()
    server.logger.info('%s cursor', cursor)
    cursor.execute("SELECT COUNT(*) FROM table_demo")
    (number_of_rows,)=cursor.fetchone()
    server.logger.info('%d number_of_rows', number_of_rows)
    cursor.close()
    connection.close()
    return "There are {} records inserted in db".format(number_of_rows)

if __name__ == "__main__":
   server.run(debug=True, host='0.0.0.0', port=5000)
