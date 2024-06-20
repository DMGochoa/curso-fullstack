from typing import Optional
from pydantic import BaseModel, Field
import datetime


class Transaction(BaseModel):
    id: Optional[int] = None
    type_id: int = Field(ge=1)
    category_id: int = Field(ge=1)
    user_id: Optional[int] = Field(ge=1)
    account_id: int = Field(ge=1)
    quantity: int = Field(ge=1)
    date: Optional[datetime.datetime] = None


class TransactionFilter(BaseModel):
    user_id: Optional[int] = None
    account_id: Optional[int] = None
    transaction_type_id: Optional[int] = None
    transaction_category_id: Optional[int] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
