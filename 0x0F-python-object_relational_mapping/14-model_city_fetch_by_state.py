#!/usr/bin/python3
"""
    Import Modules here
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session, sessionmaker


def main():
    """
        prints all city objects from the database
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
    results = session.query(State, City).join(City).order_by(City.id).all()
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
