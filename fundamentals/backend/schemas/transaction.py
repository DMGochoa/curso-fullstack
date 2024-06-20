from typing import Optional
from pydantic import BaseModel, Field
import datetime


class Transaction(BaseModel):
    id: Optional[int] = None
    type_id: int = Field(ge=1)
    account: str = Field(min_length=6, max_length=30)
    category: str = Field(min_length=6, max_length=40)
    description: str = Field(min_length=6, max_length=250)
    quantity:float = Field(ge=0)
    date: Optional[datetime.datetime] = Field(default=datetime.datetime.now(datetime.timezone.utc))


class TransactionFilter(BaseModel):
    limit: int = Field(ge=1, le=100)
    offset: int = Field(ge=0)
    account: Optional[str] = None
    category: Optional[str] = None
    type_id: Optional[int] = None
    start_date: Optional[datetime.datetime] = None
    end_date: Optional[datetime.datetime] = None
