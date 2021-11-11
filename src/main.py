from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional

from db.database import executeQuery


# id, fullname, email, gender, credit_card, credit_type
def sqlToJson(sql_data):
    json = []

    for sql in sql_data:
        json.append({
            "id": sql[0],
            "fullname": sql[1],
            "email": sql[2],
            "credit_card": sql[3],
            "credit_type": sql[4]
        })

    return json


class User(BaseModel):
    id: int = Optional
    fullname: str
    email: str
    credit_card: str
    credit_type: str


app = FastAPI()


@app.get("/")
def allUsers():
    return sqlToJson(executeQuery(action="GET"))


@app.get("/{id:int}")
def oneUser(id):
    print(id)
    return sqlToJson(executeQuery(action="GET", id=id))

