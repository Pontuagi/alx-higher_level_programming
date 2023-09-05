#!/usr/bin/python3

"""
ontains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

Base = declarative_base()


class City(Base):
    """
    inherits from Base
    links to the MySQL table cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
