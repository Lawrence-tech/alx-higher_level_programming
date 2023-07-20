#!/usr/bin/python3
"""Contains a script that prints the first State object from the database

8-model_state_fetch_first.py
    - List the first State object from the database hbtn_0e_6_usa.

Usage: ./8-model_state_fetch_first.py <db_username> <db_password> <db_name>

Connects to a MySQL database
    using the given credentials
    and retrieves all State objects from the 'states' table in the database.

The retrieved objects are printed
    to the console in ascending order of their 'id' attribute.
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the database using the provided credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    # Create a session object using the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # if the table 'states' is empty, print "Nothing"
    state = session.query(State).first()
    if state is None:
        print("Nothing")
    else:
        # Retrieve first State objects from the 'states' table
        # and print print to the console
        print("{}: {}".format(state.id, state.name))
