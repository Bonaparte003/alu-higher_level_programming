#!/usr/bin/python3
"""displays all states in database"""
import MySQLdb
import sys


if __name__ == "__main__":
    """connecting"""
    db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306)
    cr = db.cursor()
    match = sys.argv[4]
    cr.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    tables = cr.fetchall()
    for i in tables:
        print(i)
    cr.close()
    db.close()
