from config.database import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
import datetime


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    type_id = Column(Integer, ForeignKey('transaction_types.id'))
    account = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)

    type = relationship("TransactionType", back_populates="transactions")
