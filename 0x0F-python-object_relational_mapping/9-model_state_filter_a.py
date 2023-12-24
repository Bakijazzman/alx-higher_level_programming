#!/usr/bin/python3
"""
    Import Modules Here
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def main():
    """
        this functions gets arguments passed in
    """
    db_username = argv[1]
    db_password = argv[2]
    db_name = argv[3]
    db_host = "localhost"

    try:
        engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                               .format(
                                   db_username,
                                   db_password,
                                   db_host,
                                   db_name),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = Session(engine)
        states = session.query(State).filter(
                State.name.like("%a%")
                ).order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")
        session.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
