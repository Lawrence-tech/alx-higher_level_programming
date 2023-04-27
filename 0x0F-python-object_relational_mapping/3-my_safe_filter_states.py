#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
But this time,is safe from MySQL injections!
"""
import sys
import MySQLdb

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name)

    search = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (search, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
