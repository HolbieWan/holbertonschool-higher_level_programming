#!/usr/bin/python3
"""Fetch and print all rows from cities table using SQLAlchemy
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

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

    result = session.query(City, State).join(
        State, City.state_id == State.id).all()

    for city, state in result:
        print(f'{state.name}: {(city.id)} {city.name}')

    session.close()
