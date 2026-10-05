## Quick start
- cd into the project dir
``` bash
docker compose --env-file .env.example up
```
- open a browser at http://127.0.0.1:8000/todoapp/
**Note:** For the love of all that is holy please change the default passwords found in example.env by using a .env file of your own with your own credentials.

## The plan
- take an example openapi crud yaml description
- modify it for our todo app
- install fastapi and the openapi python generator in a venv

## local dev setup 
- create a python virtual environment
``` bash
python -m venv .venv
```
- activate the virtual environment in your terminal
``` bash
source .venv/bin/activate
```

## Open api Dev Setup
- got an example todo yaml from here as a start: https://github.com/alma-cdk/openapix/blob/main/examples/todo-api/schema/todo-api.yaml 
- install the python open-api generator
``` bash
pip install fastapi-code-generator
pip install fastapi
```
- generate the code
``` bash
fastapi-codegen --input petstore_api.json --output app
```
- install uv
``` bash
pip install uv
pip install "fastapi[standard]"
```
- run the dev server
``` bash
uv run fastapi dev
```
- remove the "." from the models import in the main.py

# Database Setup
Note: for local dev work I used the default sqlite db
```bash
pip install sqlalchemy alembic
```
- alembic Setup (migration tool)
``` bash
alembic init alembic
alembic revision --autogenerate -m "init"
```

# Docker setup
``` bash
docker build --tag todo .
docker run -d -p 8000:80 todo
```

# Frontend
- The frontend was created with AI. Below is the prompt and model details:
``` bash
create a single page html5 Todo app using this openapi spec.
ability to create todo
ability to mark todo as finished and delete
ability to set a reminder
list todos that have a reminder date at or before current date.
cyber punk theme.
as few libraries as possible. simple html html5 javascript
```
**Model: **GPT Sol-6.1 medium
