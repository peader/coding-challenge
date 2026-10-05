import os
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class dbTodo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    reminderDateTime = Column(DateTime)
