# Test Server
#
# Creeërt een rcp socket en geeft de koploper data als stream iedere 5 seconden.
#

import socket
import time

# run on localhost
HOST = 'localhost'
PORT = 5700

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Client connection accepted ', addr)
    while True:
        try:
            #Koploper data string
            data = str('(501\x1b 8\x1b18:31:44\x1b16:39:04\x1bRoute onbekend\x1b')
            data = data.encode('UTF-8')
            print(data)
            conn.send(data)
            time.sleep(5)
        except socket.error:
            print('Client connection closed', addr)
            break

    while False:
        conn.close()
