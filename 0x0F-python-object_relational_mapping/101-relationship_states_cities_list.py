#!/usr/bin/python3

"""
a script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def List_relationship():
    if len(argv) != 4:
        return

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    List_relationship()