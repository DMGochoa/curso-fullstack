from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class TransactionType(Base):
    __tablename__ = "transaction_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    transactions = relationship("Transaction", back_populates="type")
