#!/usr/bin/python3
"""lists all states"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    cursor = database.cursor()
    cursor.execute('SELECT * FROM states')
    tables = cursor.fetchall()
    for i in tables:
        print(i)
    cursor.close()
    database.close()
