#!/usr/bin/python3
"""
    Import Modules Here
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
        this functions gets arguments passed in
    """
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    sort_by = argv[4]
    db_port = 3306
    db_host = "localhost"

    connector = MySQLdb.connect(host=db_host, port=db_port,
                                user=username, passwd=password,
                                db=dbname, charset="utf8")
    cursor = connector.cursor()
    query = "SELECT * FROM states WHERE name = '{}'"
    passed = query.format(sort_by)
    cursor.execute(passed)
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == sort_by:
            print(row)
    cursor.close()
    connector.close()
