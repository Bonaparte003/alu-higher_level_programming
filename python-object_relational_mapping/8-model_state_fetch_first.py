#!/usr/bin/python3
""" prints the first state obj"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """connection"""
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                )
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    resul = session.query(State).first()
    if resul is not None:
        print(str(resul.id) + ":", resul.name)
    else:
        print("Nothing")
