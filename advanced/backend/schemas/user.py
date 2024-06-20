from typing import Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    id: Optional[int] = None
    username: str = Field(..., min_length=5, max_length=50)
    email:str = Field(default="example@example.com", pattern="[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}", min_length=5, max_length=50)
    password: str = Field(..., min_length=8)
    is_active: Optional[bool] = True

class UserLogin(BaseModel):
    email: str = Field(..., min_length=5, max_length=50)
    password: str = Field(..., min_length=8)
