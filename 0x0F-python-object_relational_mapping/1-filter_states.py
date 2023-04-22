#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


def main(mysql_username: str, mysql_password: str, database_name: str) -> None:
    """
    Connects to the MySQL database and retrieves all states
    with a name starting with 'N'. Prints the results to the console.
    """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py < mysql username >
              < mysql password > < database name >")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])
