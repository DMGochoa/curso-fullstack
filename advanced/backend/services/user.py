from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.user import User
from models.user import User as UserModel
from config.database import Session
from passlib.context import CryptContext
from fastapi import Depends, HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self):
        self.db = Session()

    def get_users(self):
        users = self.db.query(UserModel).all()
        data = jsonable_encoder(users)
        return JSONResponse(content=data, status_code=200)

    def get_active_user(self, id: int):
        user = self.db.query(UserModel).filter(
            UserModel.id == id, UserModel.is_active == True).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        data = jsonable_encoder(user)
        return JSONResponse(content=data, status_code=200)

    def get_inactive_user(self, id: int):
        user = self.db.query(UserModel).filter(
            UserModel.id == id, UserModel.is_active == False).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        data = jsonable_encoder(user)
        return JSONResponse(content=data, status_code=200)

    def get_user_by_email(self, email: str):
        user = self.db.query(UserModel).filter(
            UserModel.email == email, UserModel.is_active == True).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        data = jsonable_encoder(user)
        return JSONResponse(content=data, status_code=200)

    def delete_user(self, id: int):
        user = self.db.query(UserModel).filter(UserModel.id == id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        user.is_active = False
        self.db.commit()
        return JSONResponse(content={"message": "User deleted successfully"}, status_code=200)

    def update_user(self, id: int, user: User):
        user_data = user.dict()
        existing_user = self.db.query(UserModel).filter(
            UserModel.id == id).first()
        if existing_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        for key, value in user_data.items():
            setattr(existing_user, key, value)
        self.db.commit()
        return JSONResponse(content={"message": "User updated successfully"}, status_code=200)

    def create_user(self, user: User):
        hashed_password = pwd_context.hash(user.password)
        user.password = hashed_password
        new_user = UserModel(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()
        return JSONResponse(content={"message": "User created successfully"}, status_code=201)

    def activate_user(self, id: int):
        user = self.db.query(UserModel).filter(UserModel.id == id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        user.is_active = True
        self.db.commit()
        return JSONResponse(content={"message": "User activated successfully"}, status_code=200)

    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
