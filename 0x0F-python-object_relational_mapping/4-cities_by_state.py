#!/usr/bin/python3
"""
    Import Modules Here
"""
import MySQLdb
from sys import argv


def main():
    """
        this functions gets arguments passed in
    """
    db_username = argv[1]
    db_password = argv[2]
    db_name = argv[3]
    db_port = 3306
    db_host = "localhost"

    try:
        command = "SELECT cities.id, cities.name, states.name"
        command += "FROM cities LEFT JOIN states"
        command += "ON cities.states_id=states.id"
        command += "ORDER BY cities.id ASC"
        connector = MySQLdb.connect(host=db_host, port=db_port,
                                    user=db_username, passwd=db_password,
                                    db=db_name, charset="utf8")
        cursor = connector.cursor()
        cursor.execute(command)
        rows = cursor.fetchall()
        for row in rows:
            if row[1][0] == 'N':
                print(row)
        cursor.close()
        connector.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
