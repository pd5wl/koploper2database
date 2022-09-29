import socket
import etc.config as cfg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((cfg.sckthost, cfg.scktport))

def soc_conn:
    # modify data for further use
    data = s.recv(256)
    data = data.decode('UTF-8')
    data = data.replace("(", '')
    data = data.replace(")", '')
    data = data.replace("\x1b", ";")
    # Split data with use of the ; separator
    datalist = data.split(';')
    return datalist
