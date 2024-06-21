#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a Base instance for declarative class definitions
Base = declarative_base()

class State(Base):
    """State class that links to the MySQL table states"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
