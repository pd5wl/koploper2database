import mysql.connector
# from mysql.connector import errorcode
import etc.config as cfg

mydb = mysql.connector.connect(**cfg.mysql)
mycursor = mydb.cursor()


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
