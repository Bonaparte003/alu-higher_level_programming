#!/usr/bin/python3
"""lists all states"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    cursor = database.cursor()
    cursor.execute('SELECT * FROM states')
    tables = cursor.fetchall()
    for i in tables:
        print(i)
    cursor.close()
    database.close()
