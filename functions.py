import mysql.connector
# from mysql.connector import errorcode
import etc.config as cfg
import os

mydb = mysql.connector.connect(**cfg.mysql)
mycursor = mydb.cursor()

savefile = os.path.join(cfg.save_path, cfg.file_name)
def dbsql(datalist):
    # take list to set values for SQL proccessing
    loc = datalist[0]
    blok = datalist[1]
    mod_time = datalist[2]
    real_time = datalist[3]
    route = datalist[4]
    # procces SQL for insertion
    mycursor.execute("UPDATE output SET blok = %s, mod_time = '%s', real_time = '%s', route = '%s' WHERE loc = %s" %
                     (blok, mod_time, real_time, route, loc))
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")


# Write to file
# 1 for append to file. 0 create a new file every time you start
if cfg.op_fileadd == 1:
    f = open(savefile, "a")
#    line1 = ("Opmaak van de data", '\n')
#    kop1 = ','.join(str(v) for v in line1)
#    line2 = ("loc, time, blok, route", '\n')
#    kop2 = ','.join(str(v) for v in line2)
#    f.write(kop1)
#    f.write(kop2)
else:
    f = open(savefile, "w")
    line1 = ("Opmaak van de data", '\n')
    kop1 = ','.join(str(v) for v in line1)
    line2 = ("loc, time, blok, route", '\n')
    kop2 = ','.join(str(v) for v in line2)
    f.write(kop1)
    f.write(kop2)

# Write the file
def wrtfile(datalist):
    # take list to set values for SQL proccessing
    loc = datalist[0]
    blok = datalist[1]
    mod_time = datalist[2]
    real_time = datalist[3]
    route = datalist[4]
    # procces write to file
    if cfg.kl_tijd == 1:
        line = (loc, ",", mod_time, ",", blok, ",", route, '\n')
        values = ','.join(str(v) for v in line)
        f.write(values)
    else:
        line = (loc, ",", real_time, ",", blok, ",", route, '\n')
        values = ','.join(str(v) for v in line)
        f.write(values)
