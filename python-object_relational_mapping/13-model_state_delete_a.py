#!/usr/bin/python3
"""deletes all State objects with a name containing
 the letter a from the database hbtn_0e_6_usa
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

    delete_state_with_a = session.query(
        State).filter(State.name.like('%a%')).all()

    if delete_state_with_a:
        for State in delete_state_with_a:
            session.delete(State)
        session.commit()
    else:
        print("Not found")

    session.close()
