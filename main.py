# De TCP client
#
# Lees de data, knipt het op en slaat het op in een database.
#
import socket


# HOST = '192.168.68.108'
HOST = 'localhost'
PORT = 5700

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(256)
    data = data.decode('UTF-8')
    print(data)

while False:
    s.close()
