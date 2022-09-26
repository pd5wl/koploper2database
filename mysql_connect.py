import mysql.connector
# from mysql.connector import errorcode
import config as cfg

mydb = mysql.connector.connect(**cfg.mysql)
mycursor = mydb.cursor()

