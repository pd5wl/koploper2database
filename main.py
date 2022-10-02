# De TCP client
#
# Lees en knip de data op en stuur het naar de handler.
#
import etc.config as cfg
import socket

if cfg.op_select == 1:
    from lib import dbhandeling as func
else:
    from lib import filehandeling as func

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((cfg.sckthost, cfg.scktport))

while True:
    # modify data for further use
    data = s.recv(512)
    data = data.decode('UTF-8')
    data = data.replace("(", '')
    data = data.replace(")", '')
    data = data.replace("\x1b", ";")
    # Split data with use of the ; separator
    datalist = data.split(';')
    # Traceer de trein Add-On
    if cfg.trace_train == 1:
        func.trackloc(datalist)
    else:
        pass
    # Pass the data to the handler
    func.passdata(datalist)

while False:
    s.close()
    print("Connection lost")
