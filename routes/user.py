from fastapi import APIRouter

from models.user import User
from config.db import db
from schemas.user import userEntity, usersEntity

user = APIRouter()


@user.post("/create")
async def create_user(user: User):
    db.fastapi.user.insert_one(dict(user))
    return {"message": "User created"}


@user.get("/get_users")
async def get_user():
    print(db.fastapi.user.find())
    print(usersEntity(db.fastapi.user.find()))
    return usersEntity(db.fastapi.user.find())


@user.get("/get_users")
async def get_user():
    print(db.fastapi.user.find())
    print(usersEntity(db.fastapi.user.find()))
    return usersEntity(db.fastapi.user.find())

