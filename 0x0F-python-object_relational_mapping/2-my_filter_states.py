#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    c = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    c.execute(query, (state_name,))

    rows = c.fetchall()
    for row in rows:
        print(row)

    c.close()
    db.close()
