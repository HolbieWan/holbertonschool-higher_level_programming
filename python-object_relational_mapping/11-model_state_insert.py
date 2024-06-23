#!/usr/bin/python3
"""Fetch and prints the State object with the name passed as
 argument from the database hbtn_0e_6_usa
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

    # Add rows to the state table
    new_states = [
        State(name="Louisiana")
    ]

    # Add the new states to the session
    session.add_all(new_states)

    # Commit the transaction to the database
    session.commit()

    state_like_louisiana = session.query(State).filter(
        State.name == 'Louisiana').all()

    if state_like_louisiana:
        for State in state_like_louisiana:
            print(f'{State.id}')
    else:
        print("Not found")

    session.close()
