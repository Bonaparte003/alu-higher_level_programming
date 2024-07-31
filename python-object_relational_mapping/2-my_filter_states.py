#!/usr/bin/python3
"""lists states"""
import MySQLdb
import sys


if __name__ == "__main__":
    """starting with the conections"""
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306)
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    tables = cr.fetchall()
    for r in tables:
        print(r)
    cr.close()
    db.close()
