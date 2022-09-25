import mysql.connector
# from mysql.connector import errorcode
import config as cfg

mydb = mysql.connector.connect(**cfg.mysql)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mydb.close()
