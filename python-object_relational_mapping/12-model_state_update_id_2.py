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

    new_state_name = 'New Mexico'

    update_state_name = session.query(State).filter(
        State.id == 2).all()

    if update_state_name:
        for State in update_state_name:
            State.name = new_state_name
            session.commit()
    else:
        print("Not found")

    session.close()
