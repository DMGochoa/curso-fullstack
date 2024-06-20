from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class TransactionCategory(Base):
    __tablename__ = "transaction_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)
    transactions = relationship("Transaction", back_populates="category")
