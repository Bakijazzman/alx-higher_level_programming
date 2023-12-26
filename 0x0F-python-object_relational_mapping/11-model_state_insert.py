#!/usr/bin/python3
"""
    Import Module Here
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """
        script that adds louisiana state to the database
    """
    db_username = argv[1]
    db_password = argv[2]
    db_name = argv[3]
    db_host = "localhost"

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(
                                db_username,
                                db_password,
                                db_host,
                                db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    if new:
        print(new.id)
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    main()
