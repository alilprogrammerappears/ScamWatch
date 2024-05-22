import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='scamwatchdb.c9eg4kuesca7.us-east-2.rds.amazonaws.com',
        database='scamwatchdb',
        user='admin',
        password='scamwatch'
    )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
