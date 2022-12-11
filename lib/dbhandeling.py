# Database handeling

import mysql.connector
# from mysql.connector import errorcode
import etc.config as cfg

# Connect to databse server
mydb = mysql.connector.connect(**cfg.mysql)
mycursor = mydb.cursor()

# Build SQL
# passdata
query = "\
            INSERT INTO output (loc, blok, mod_time, real_time, route) \
            VALUES (%s, %s, %s, %s, %s) \
            ON DUPLICATE KEY UPDATE blok = values(blok), mod_time = values(mod_time), real_time = values(real_time), \
            route = values(route)"
# trackloc
sql_lees = "SELECT blok FROM output WHERE loc = %s"
sql_update = " UPDATE output SET vorig_blok = '%s' WHERE loc = '%s' "

# Write to database

def passdata(datalist):
    loc = datalist[0]
    blok = datalist[1]
    mod_time = datalist[2]
    real_time = datalist[3]
    route = datalist[4]
    values = (loc, blok, mod_time, real_time, route)
# procces SQL for insertion
    mycursor.execute(query, values)
    mydb.commit()
    if cfg.dbg_print == 1:
        print("Record ingevoegd of bijgewerkt")
    else:
        pass


def trackloc(datalist):
    update_data = [int(datalist[0]),]
    if cfg.dbg_print == 1:
        print("Lees laatste blok : ", update_data)
    else:
        pass
    mycursor.execute(sql_lees, update_data)
    record = mycursor.fetchone()
    print("Gelezen record : ", record)
    vorig_blok = record[0]
    update_data.insert(0, vorig_blok)
    print(update_data)
    if cfg.dbg_print == 1:
        print("Data om in de DB te verwerken : ", update_data)
    else:
        pass
    mycursor.execute(sql_update, update_data)
    mydb.commit()
    if cfg.dbg_print == 1:
        print("Vorig blok geupdate")
    else:
        pass
    return
