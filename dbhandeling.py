# Database handeling

import mysql.connector
# from mysql.connector import errorcode
import etc.config as cfg

mydb = mysql.connector.connect(**cfg.mysql)
mycursor = mydb.cursor()

def dbsql(datalist):
    loc = datalist[0]
    blok = datalist[1]
    mod_time = datalist[2]
    real_time = datalist[3]
    route = datalist[4]
    values = (loc, blok, mod_time, real_time, route)
    # procces SQL for insertion
    query = "\
            INSERT INTO output (loc, blok, mod_time, real_time, route) \
            VALUES (%s, %s, %s, %s, %s) \
            ON DUPLICATE KEY UPDATE blok = values(blok), mod_time = values(mod_time), real_time = values(real_time), \
            route = values(route)"
    mycursor.execute(query, values)
    mydb.commit()
    #print(mycursor.rowcount, "record(s) affected")

