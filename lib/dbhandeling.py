# Database handeling

import mysql.connector
# from mysql.connector import errorcode
import etc.config as cfg

# Connect to databse server
mydb = mysql.connector.connect(**cfg.mysql)
mycursor = mydb.cursor()

# Write to database


def passdata(datalist):
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

    if cfg.dbg_print == 1:
        print("Bla bla car")
    else:
        pass
