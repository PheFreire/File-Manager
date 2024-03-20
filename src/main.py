from typing import Union

from fastapi import FastAPI

from domain.controller.core import get_dependency_injections_controller
from domain.controller.database import create_database_controller

app = FastAPI()


@app.get("/")
def hello_world():
    dependency_injections = get_dependency_injections_controller()
    database_executor_provider = create_database_controller(dependency_injections)

    database_executor_provider.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s);",
        ('Phelipe', 'pheprogrammer@gmail.com', 'pato123'),
        False
    )

    breakpoint()
    return {"Hello": "World"}
