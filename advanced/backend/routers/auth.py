from fastapi import APIRouter, HTTPException
from utils.jwt_manager import create_token
from schemas.user import UserLogin
from services.user import UserService
import json

auth_router = APIRouter()

@auth_router.post("/login", tags=['auth'], response_model=dict, status_code=200)
def login(user: UserLogin):
    user_service = UserService()
    db_user = user_service.get_user_by_email(user.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = json.loads(db_user.body.decode())
    print(user_data)
    if not user_service.verify_password(user.password, user_data['password']):
        raise HTTPException(status_code=400, detail="Invalid password")
    try:
        role = user_data['role']
    except:
        role = "admin"
    token = create_token({"user_id": user_data['id'], "role": role})
    return {"token": token}
