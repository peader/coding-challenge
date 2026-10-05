import os

from dbmodels import dbTodo, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Todo


class repository:
    def __init__(self):
        DATABASE_URL = os.environ.get("DATABASE_URL")
        if DATABASE_URL == None:
            DATABASE_URL = "sqlite:///app.db"
        engine = create_engine(DATABASE_URL)
        self.Session = sessionmaker(bind=engine)
        # Create the database table if it doesn't already exist
        Base.metadata.create_all(engine)

    def __del__(self):
        self.session.close()

    def createTodo(self, newTodo: Todo):
        try:
            session = self.Session()
            dbNewTodo = dbTodo(name=newTodo.name, reminderDateTime=newTodo.reminder)
            session.add(dbNewTodo)
            session.commit()
            return dbNewTodo
        finally:
            print("get that session out of here")
            session.close()

    def deleteTodo(self, id):
        try:
            session = self.Session()
            todoToDelete = session.query(dbTodo).filter_by(id=id).first()
            if todoToDelete == None:
                return
            session.delete(todoToDelete)
            session.commit()
        finally:
            print("get that session out of here")
            session.close()

    def updateTodo(self, updatedTodo: Todo):
        try:
            session = self.Session()
            dbTodoToUpdate = session.query(dbTodo).filter_by(id=updatedTodo.id).first()
            if dbTodoToUpdate == None:
                return
            dbTodoToUpdate.name = updatedTodo.name
            dbTodoToUpdate.tag = updatedTodo.tag
            dbTodoToUpdate.reminderDateTime = updatedTodo.reminder
            session.commit()
        finally:
            print("get that session out of here")
            session.close()

    def fetchAllTodos(self):
        try:
            session = self.Session()
            returnListTodos = []
            todos = session.query(dbTodo).all()
            for t in todos:
                returnListTodos.append(
                    Todo(
                        id=t.id,
                        name=t.name,
                        reminder=t.reminderDateTime,
                    )
                )
            return returnListTodos
        finally:
            print("get that session out of here")
            session.close()


# test = repository()
# testControllerTodo = Todo(123, "plumber")
# test.createTodo()
# test.fetchAllTodos()
