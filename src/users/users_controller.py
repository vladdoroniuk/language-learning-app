from fastapi import APIRouter
from typing import List
from users.users_model import User
import users.users_service as users_service

router = APIRouter()


@router.get("/", response_model=List[User])
async def get_users():
    users = await users_service.get_users()
    return users


@router.get("/{user_id}")
async def get_user(user_id: int):
    users = await users_service.get_user()
    return users


@router.post("/", response_model=User)
async def create_user(user: User):
    await users_service.create_user(user)
    return user


""" @router.put("/{user_id}")
def update_user(user_id: int):
    # TODO: Implement logic to update a specific user in the database
    return {"message": f"Update user with ID {user_id}"}


@router.delete("/{user_id}")
def delete_user(user_id: int):
    # TODO: Implement logic to delete a specific user from the database
    return {"message": f"Delete user with ID {user_id}"} """
