import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='godb',
                                             user='root',
                                             password='root')
    except Error as e:
        print("Error while connecting to MySQL", e)
    return connection