
FROM python:3.14


WORKDIR /code


RUN pip install "fastapi[standard]" pydantic sqlalchemy pymysql 
  


COPY ./app /code/app
COPY ./frontend /code/frontend


CMD ["fastapi", "run", "app/main.py", "--port", "80"]
