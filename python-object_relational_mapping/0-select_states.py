#!/usr/bin/python3
"""prints all the states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def states():
    """gives all the states"""
    database = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    cursor = database.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    records = cursor.fetchall()
    for data in records:
        print(data)

    cursor.close()
    database.close()


if __name__ == "__main__":
    states()
