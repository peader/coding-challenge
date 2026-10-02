from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class dbTodo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    reminderDateTime = Column(DateTime)


# Create a SQLite database engine (file named 'app.db')
engine = create_engine("sqlite:///app.db")
# Create tables in the database (if they don’t exist)
Base.metadata.create_all(engine)
