import etc.config as cfg
import os
import datetime

savefile = os.path.join(cfg.save_path, cfg.file_name)

# Write to file
now = datetime.datetime.now()
# 1 for append to file. 0 create a new file every time you start
if cfg.op_fileadd == 1:
    f = open(savefile, "a")
    line1 = ("Aanmaak datum :", now.strftime("%Y-%m-%d %H:%M:%S"), '\n')
    kop1 = ','.join(str(v) for v in line1)
#    line2 = ("loc, blok, time, route", '\n')
#    kop2 = ','.join(str(v) for v in line2)
    f.write(kop1)
#    f.write(kop2)
    f.flush()
else:
    f = open(savefile, "w")
    line1 = ("Aanmaak datum :", now.strftime("%Y-%m-%d %H:%M:%S"), '\n')
    kop1 = ' '.join(str(v) for v in line1)
    line2 = ("loc, blok, time, route", '\n')
    kop2 = ' '.join(str(v) for v in line2)
    f.write(kop1)
    f.write(kop2)
    f.flush()

def wrtfile(datalist):  # Write the file
    # take list to set values for SQL proccessing
    loc = datalist[0]
    blok = datalist[1]
    mod_time = datalist[2]
    real_time = datalist[3]
    route = datalist[4]
    # procces write to file
    if cfg.kl_tijd == 1:
        line = (loc, blok, mod_time, route, '\n')
        values = ','.join(str(v) for v in line)
        f.write(values)
        f.flush()
    else:
        line = (loc, blok, real_time, route, '\n')
        values = ','.join(str(v) for v in line)
        f.write(values)
        f.flush()
