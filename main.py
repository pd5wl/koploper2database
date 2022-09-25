# De TCP client
#
# Lees de data, knipt het op en update het in een database.
#
import socket


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
    route = datalist[4]
    print("Locomotief", loc, "staat in blok", blok, "en volgt route", route)

while False:
    s.close()
