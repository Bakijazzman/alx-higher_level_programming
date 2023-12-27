#!/usr/bin/python3
"""
Import Modules here
"""
from sys import argv
from sqlalchemy import (create_engine)
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import Session, sessionmaker


def main():
    """
    function that prints states and the corresponding cities
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
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
    session.close()


if __name__ == "__main__":
    main()
