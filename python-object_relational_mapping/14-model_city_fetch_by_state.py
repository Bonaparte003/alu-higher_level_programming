#!/usr/bin/python3
"""contains all the modules in the ORM with a"""
from sqlalchemy import asc, create_engine
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    creator = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(creator)
    Session = sessionmaker(bind=creator)
    session = Session()
    resul = session.query(City).order_by(City.id).all()
    for i in resul:
        st = session.query(State).filter(
                State.id == i.state_id
                ).one()
        print(st.name + ": " + "(" + str(i.id) + ")" + i.name)
