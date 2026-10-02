from datetime import datetime

from dbmodels import dbTodo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Todo


class repository:
    def __init__(self):
        engine = create_engine("sqlite:///app.db")
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def __del__(self):
        print("get that session out of here")
        self.session.close()

    def createTodo(self, newTodo: Todo):
        current_dateTime = datetime.now()
        dbNewTodo = dbTodo(name=newTodo.name, reminderDateTime=current_dateTime)
        self.session.add(dbNewTodo)
        self.session.commit()
        return dbNewTodo

    def fetchAllTodos(self):
        todos = self.session.query(dbTodo).all()
        for t in todos:
            print(t.name)


test = repository()
# testControllerTodo = Todo(123, "plumber")
# test.createTodo()
test.fetchAllTodos()
