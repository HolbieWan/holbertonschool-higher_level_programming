#!/usr/bin/python3
"""Fetch and print the State object that contain the letter (a)
 from states table in the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_with_a = session.query(State).filter(State.name.like('%a%')).all()

    if state_with_a:
        for State in state_with_a:
            print(f'{State.id}: {State.name}')

    session.close()
