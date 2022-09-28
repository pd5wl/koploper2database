# De TCP client
#
# Lees de data, knipt het op en update het in een database.
#
import socket
import etc.config as cfg

if cfg.op_select == 1:
    import dbhandeling as func
else:
    import filehandeling as func

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((cfg.sckthost, cfg.scktport))

while True:
    # modify data for further use
    data = s.recv(256)
    data = data.decode('UTF-8')
    data = data.replace("(", '')
    data = data.replace(")", '')
    data = data.replace("\x1b", ";")
    # Split data with use of the ; separator
    datalist = data.split(';')

    if cfg.op_select == 1:
        # call sql funstion
        func.dbsql(datalist)
    else:
        # write file
        func.wrtfile(datalist)

while False:
    s.close()
    print("Connection lost")
