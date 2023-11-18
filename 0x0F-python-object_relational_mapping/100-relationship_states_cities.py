#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    db_inp = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_inp)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    call_state = State(name='California')
    app_city = City(name='San Francisco')
    call_state.cities.append(app_city)

    session.add(call_state)
    session.commit()
    session.close()
