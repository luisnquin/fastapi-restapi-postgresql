from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI

from db.database import executeQuery


# id, fullname, email, gender, credit_card, credit_type
def jsonifySql(sql_data):
    json = []

    for sql in sql_data:
        json.append({
            "id": sql[0],
            "fullname": sql[1],
            "email": sql[2],
            "gender": sql[3],
            "credit_card": sql[4],
            "credit_type": sql[5]
        })

    return json


class User(BaseModel):
    id: Optional[int] = False
    fullname: str
    email: str
    gender: str
    credit_card: str
    credit_type: str


app = FastAPI()


@app.get("/")
def allUsers():
    return jsonifySql(executeQuery(action="GET"))


@app.get("/{id:int}")
def oneUser(id):
    print(id)
    return jsonifySql(executeQuery(action="GET", id=id))


@app.post("/")
def addUser(user: User):
    newuser = [user.fullname, user.email, user.email,
               user.credit_card, user.credit_type]

    return jsonifySql(executeQuery(action="POST", userdata=newuser))


@app.put("/{id:int}")
def updateUser(id, user: User):
    if user.id:
        newuser = [user.id, user.fullname, user.email, user.gender,
                   user.credit_card, user.credit_type]
    else:
        newuser = [user.fullname, user.email, user.gender,
                   user.credit_card, user.credit_type]

    return jsonifySql(executeQuery(action="PUT", id=id, userdata=newuser))


@app.delete("/{id:int}")
def deleteUser(id):
    return jsonifySql(executeQuery(action="DELETE", id=id))
