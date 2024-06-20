from typing import Optional
from pydantic import BaseModel, Field

class TransactionType(BaseModel):
    id: Optional[int] = None
    name: str
