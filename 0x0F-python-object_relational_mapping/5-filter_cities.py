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
    state = argv[4]
    db_port = 3306
    db_host = "localhost"

    try:
        command = "SELECT cities.name "
        command += "FROM cities JOIN states "
        command += "ON cities.state_id = states.id "
        command += "WHERE states.name = %s "
        command += "ORDER BY cities.id ASC"
        connector = MySQLdb.connect(host=db_host, port=db_port,
                                    user=db_username, passwd=db_password,
                                    db=db_name, charset="utf8")
        cursor = connector.cursor()
        cursor.execute(command, (state, ))
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(row[0])
        print(", ".join(result))
        cursor.close()
        connector.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
