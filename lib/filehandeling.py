import etc.config as cfg
import os
import datetime

savefile = os.path.join(cfg.save_path, cfg.file_name)
now = datetime.datetime.now()

# Write to file
# Append to file or create a new file every time you start

if cfg.op_fileadd == 1:
    f = open(savefile, "a")
    line1 = ("Aanmaak datum :", now.strftime("%Y-%m-%d %H:%M:%S"))
    kop1 = ','.join(str(v) for v in line1)
    line2 = "loc, blok, time, route"
    kop2 = ','.join(str(v) for v in line2)
    f.write(kop1)
    f.write('\n')
    f.write(kop2)
    f.write('\n')
    if cfg.dbg_print == 1:
        print(kop1)
        print(kop2)
    else:
        pass
    f.flush()
else:
    f = open(savefile, "w")
    line1 = ("Aanmaak datum :", now.strftime("%Y-%m-%d %H:%M:%S"))
    kop1 = ' '.join(str(v) for v in line1)
    line2 = "loc, blok, time, route"
    kop2 = ' '.join(str(v) for v in line2)
    f.write(kop1)
    f.write('\n')
    f.write(kop2)
    f.write('\n')
    if cfg.dbg_print == 1:
        print(kop1)
        print(kop2)
    else:
        pass
    f.flush()

# Write to a file


def passdata(datalist):
    loc = datalist[0]
    blok = datalist[1]
    mod_time = datalist[2]
    real_time = datalist[3]
    route = datalist[4]

# write with model time or real time
    if cfg.kl_tijd == 1:
        line = (loc, blok, mod_time, route)
        values = ','.join(str(v) for v in line)
        f.write(values)
        f.write('\n')
        if cfg.dbg_print == 1:
            print(values)
        else:
            pass
        f.flush()
    else:
        line = (loc, blok, real_time, route)
        values = ','.join(str(v) for v in line)
        f.write(values)
        f.write('\n')
        if cfg.dbg_print == 1:
            print(values)
        else:
            pass
        f.flush()
