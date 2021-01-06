"""
Write python code to integrate SQL with Python by importing the MySQL module
"""
import mysql.connector as sql
import sys

if __name__ == '__main__':
    try:
        connection = sql.connect(host='localhost', user='root', password='3244')
        connection.close()

    except sql.Error as e:
        print("Error while connecting to MySQL Server: ", e)
        sys.exit()

    connection = sql.connect(host='localhost', user='root', password='3244')
    connection.cmd_query("use tstdata;")
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    connection.close()
