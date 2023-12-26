#!/usr/bin/python3
"""
    Import Modules Here
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import (create_engine)


def main():
    """
        Updates states name of a given id
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.id == 2).first()
    if states:
        states.name = "New Mexico"
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
