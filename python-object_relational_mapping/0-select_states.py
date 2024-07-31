#!/usr/bin/python3
"""function that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


database = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = database.cursor()
cursor.execute("SELECT * FROM states ORDER BY id")
row = cursor.fetchall()
for i in row:
    print(i)