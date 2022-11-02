import psycopg2
import etc.config as cfg

conn = psycopg2.connect(**cfg.postgre)
cursor = conn.cursor()

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
    cursor.execute(query, values)
    conn.commit()

    if cfg.dbg_print == 1:
        print("Record ingevoegd of bijgewerkt")
    else:
        pass
