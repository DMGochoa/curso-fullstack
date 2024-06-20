from config.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    interest = Column(Float, nullable=False)
    management_fee = Column(Float, nullable=False)
    cutoff_day = Column(Integer, nullable=False)
    creation_date = Column(DateTime, nullable=False, default=datetime.datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    transactions = relationship("Transaction", back_populates="account")
    user = relationship("User", back_populates="accounts")
