## The plan
- take an example openapi crud yaml description
- modify it for our todo app
- install fastapi and the openapi python generator in a venv

## Setup 
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

