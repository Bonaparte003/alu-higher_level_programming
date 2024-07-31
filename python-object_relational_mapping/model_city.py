#!/usr/bin/python3
"""moduel create_city making"""

from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """creation of class City"""
    __tablename__ = 'cities'
    id = Column(
        Integer, autoincrement=True, nullable=False,
        primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
