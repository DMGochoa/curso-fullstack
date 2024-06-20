from fastapi import APIRouter, Path

from schemas.user import User
from services.user import UserService

user_router = APIRouter()
base_path = "/users"

@user_router.get(base_path)
def get_users():
    return UserService().get_users()

@user_router.get(base_path + "/{id}/active")
def get_active_user(id: int):
    return UserService().get_active_user(id)

@user_router.get(base_path + "/{id}/inactive")
def get_inactive_user(id: int):
    return UserService().get_inactive_user(id)

@user_router.delete(base_path + "/{id}")
def delete_user(id: int = Path(ge=1)):
    return UserService().delete_user(id)

@user_router.put(base_path + "/{id}")
def update_user(id: int, user: User):
    return UserService().update_user(id, user)

@user_router.post(base_path)
def create_user(user: User):
    return UserService().create_user(user)

def activate_user(id: int):
    return UserService().activate_user(id)
