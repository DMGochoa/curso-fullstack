from config.database import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    account_id = Column(Integer, ForeignKey('accounts.id'))
    category_id = Column(Integer, ForeignKey('transaction_categories.id'))
    type_id = Column(Integer, ForeignKey('transaction_types.id'))
    quantity = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)

    account = relationship("Account", back_populates="transactions")
    category = relationship("TransactionCategory", back_populates="transactions")
    type = relationship("TransactionType", back_populates="transactions")
    user = relationship("User", back_populates="transactions")
