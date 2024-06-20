from typing import Optional
from pydantic import BaseModel, Field

class TransactionType(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=6, max_length=40)
