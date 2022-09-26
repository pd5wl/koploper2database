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
            # Koploper data string
            data = str('(501\x1b 8\x1b01:31:44\x1b06:39:04\x1bRoute onbekend\x1b')
            data = data.encode('UTF-8')
            print(data)
            conn.send(data)
            time.sleep(2)

            # Koploper data string
            data = str('(411\x1b11\x1b02:31:44\x1b05:39:04\x1bRoute onbekend\x1b')
            data = data.encode('UTF-8')
            print(data)
            conn.send(data)
            time.sleep(1)

            # Koploper data string
            data = str('(501\x1b 12\x1b03:31:44\x1b04:39:04\x1bRoute onbekend\x1b')
            data = data.encode('UTF-8')
            print(data)
            conn.send(data)
            time.sleep(1)

            # Koploper data string
            data = str('(502\x1b13\x1b04:31:44\x1b03:39:04\x1bRoute onbekend\x1b')
            data = data.encode('UTF-8')
            print(data)
            conn.send(data)
            time.sleep(1)

            # Koploper data string
            data = str('(502\x1b19\x1b05:31:44\x1b02:39:04\x1bRoute onbekend\x1b')
            data = data.encode('UTF-8')
            print(data)
            conn.send(data)
            time.sleep(4)

            # Koploper data string
            data = str('(411\x1b11\x1b06:31:44\x1b01:39:04\x1bRoute onbekend\x1b')
            data = data.encode('UTF-8')
            print(data)
            conn.send(data)
            time.sleep(6)
        except socket.error:
            print('Client connection closed', addr)
            break

    while False:
        conn.close()
