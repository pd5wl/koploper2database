# De TCP client
#
# Lees de data, knipt het op en update het in een database.
#
import socket
import mysql.connector
# from mysql.connector import errorcode
import config as cfg

mydb = mysql.connector.connect(**cfg.mysql)
mycursor = mydb.cursor()

HOST = 'localhost'
PORT = 5700

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(256)
    data = data.decode('UTF-8')
    data = data.replace("(", '')
    data = data.replace(")", '')
    data = data.replace("\x1b", ";")
    # ; separator
    datalist = data.split(';')
    print(datalist)
    loc = datalist[0]
    blok = datalist[1]
    mod_time = datalist[2]
    real_time = datalist[3]
    route = datalist[4]
    print("Locomotief", loc, "staat om", mod_time, "in blok", blok, "en volgt route", route)
    # SQL
    mycursor.execute("UPDATE output SET blok = %s, mod_time = '%s', real_time = '%s', route = '%s' WHERE loc = %s" %
                     (blok, mod_time, real_time, route, loc))
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

while False:
    s.close()
    print("Connection lost")
