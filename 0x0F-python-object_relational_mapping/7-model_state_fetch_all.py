#!/usr/bin/python3

if __name__ == "__main__":

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
from sqlalchemy.ext.declarative import declarative_base

    i = sys.argv
    if len(i) < 4:
        exit(1)

    # Database connection
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(i[1], i[2], i[3]))
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all State objects and display them
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
