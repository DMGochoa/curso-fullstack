from typing import Optional
from pydantic import BaseModel, Field

class TransactionCategory(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = Field(None, min_length=16, max_length=250)
