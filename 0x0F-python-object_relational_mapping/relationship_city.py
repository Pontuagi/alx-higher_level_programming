#!/usr/bin/python3

"""
Improve the files model_city.py
"""

from relationship_state import Base
from sys import argv
from sqlalchemy import Column, String, ForeignKey, Integer


class City(Base):
    """
    class City
    inherits from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
