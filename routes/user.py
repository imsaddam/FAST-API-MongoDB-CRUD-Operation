from fastapi import APIRouter

from models.user import User
from config.db import db
from schemas.user import userEntity, usersEntity
from bson.objectid import ObjectId

user = APIRouter()


@user.post("/create_user")
async def create_user(user: User):
    db.fastapi.user.insert_one(dict(user))
    return {"message": "User created"}


@user.get("/get_users")
async def get_user():
    print(db.fastapi.user.find())
    print(usersEntity(db.fastapi.user.find()))
    return usersEntity(db.fastapi.user.find())


@user.put("/update_user/{id}")
async def update_user(id, user: User):
    db.fastapi.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })

    return userEntity(db.fastapi.user.find_one({"_id": ObjectId(id)}))


@user.delete("/delete_user/{id}")
async def delete_user(id, user: User):
    return userEntity(db.fastapi.user.find_one_and_delete({"_id": ObjectId(id)}))
