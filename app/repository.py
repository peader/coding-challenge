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
        Session = sessionmaker(bind=engine)
        self.session = Session()
        # Create the database table if it doesn't already exist
        Base.metadata.create_all(engine)

    def __del__(self):
        print("get that session out of here")
        self.session.close()

    def createTodo(self, newTodo: Todo):
        dbNewTodo = dbTodo(name=newTodo.name, reminderDateTime=newTodo.reminder)
        self.session.add(dbNewTodo)
        self.session.commit()
        return dbNewTodo

    def deleteTodo(self, id):
        todoToDelete = self.session.query(dbTodo).filter_by(id=id).first()
        if todoToDelete == None:
            return
        self.session.delete(todoToDelete)
        self.session.commit()

    def updateTodo(self, updatedTodo: Todo):
        dbTodoToUpdate = self.session.query(dbTodo).filter_by(id=updatedTodo.id).first()
        if dbTodoToUpdate == None:
            return
        dbTodoToUpdate.name = updatedTodo.name
        dbTodoToUpdate.tag = updatedTodo.tag
        dbTodoToUpdate.reminderDateTime = updatedTodo.reminder
        self.session.commit()

    def fetchAllTodos(self):
        returnListTodos = []
        todos = self.session.query(dbTodo).all()
        for t in todos:
            returnListTodos.append(
                Todo(
                    id=t.id,
                    name=t.name,
                    reminder=t.reminderDateTime,
                )
            )
        return returnListTodos


# test = repository()
# testControllerTodo = Todo(123, "plumber")
# test.createTodo()
# test.fetchAllTodos()
