from typing import Optional
from pydantic import BaseModel, Field
import datetime

class Account(BaseModel):
    id: Optional[int] = None
    name: str
    interest: float = Field(ge=0)
    management_fee: float = Field(ge=0)
    cutoff_day: int = Field(ge=1, le=28)
    creation_date: Optional[datetime.date] = Field(default=datetime.date.today(), ge=datetime.date.today())
    user_id: int
