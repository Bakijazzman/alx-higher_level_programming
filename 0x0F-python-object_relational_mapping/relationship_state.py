#!/usr/bin/python3
"""
    Import Modules here
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
        A class that inherits from the declarative base
        __tablename__ = name of the sql table
        id = state id
        name = state name
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade="all, delete")
