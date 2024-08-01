#!/usr/bin/python3
"""  lists all states """
import MySQLdb
import sys


if __name__ == "__main__":
    """connects"""
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    cr = db.cursor()
    cr.execute(
        "SELECT cities.id, cities.name, states.name FROM "
        "cities INNER JOIN states ON states.id = cities.state_id"
        )
    tables = cr.fetchall()
    for r in tables:
        print(r)
    cr.close()
    db.close()
