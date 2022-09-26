# De TCP client
#
# Lees de data, knipt het op en update het in een database.
#
import socket
import functions as func
import etc.config as config

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((config.sckthost, config.scktport))

while True:
    # modify data for further use
    data = s.recv(256)
    data = data.decode('UTF-8')
    data = data.replace("(", '')
    data = data.replace(")", '')
    data = data.replace("\x1b", ";")
    # Split data with use of the ; separator
    datalist = data.split(';')
    # call sql funstion
    func.dbsql(datalist)

while False:
    s.close()
    print("Connection lost")
