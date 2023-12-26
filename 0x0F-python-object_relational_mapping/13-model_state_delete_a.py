#!/usr/bin/python3
"""
    Import Modules here
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import (create_engine)


def main():
    """
        deletes an entry from a database
    """
    db_username = argv[1]
    db_password = argv[2]
    db_name = argv[3]
    db_host = "localhost"

    engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                           .format(
                               db_username,
                               db_password,
                               db_host,
                               db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    states = session.query(State).filter(State.name.contains('a')).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
