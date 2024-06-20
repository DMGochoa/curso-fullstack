from sqlalchemy.exc import NoResultFound
from fastapi.responses import JSONResponse
from datetime import datetime
from sqlalchemy.orm import joinedload
from sqlalchemy import func
from schemas.transaction import TransactionFilter
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from schemas.transaction import Transaction
from models.transaction import Transaction as TransactionModel
from models.account import Account as AccountModel
from models.user import User as UserModel
from models.transaction_type import TransactionType as TransactionTypeModel
from models.transaction_category import TransactionCategory as TransactionCategoryModel
from config.database import Session


class TransactionService:
    def __init__(self):
        self.db = Session()

    def create(self, transaction_data: Transaction):
        try:
            self._check_resource_existence(
                AccountModel, transaction_data.account_id, "Account")
            self._check_resource_existence(
                UserModel, transaction_data.user_id, "User")
            self._check_resource_existence(
                TransactionCategoryModel, transaction_data.category_id, "Transaction category")
            self._check_resource_existence(
                TransactionTypeModel, transaction_data.type_id, "Transaction type")

            new_transaction = TransactionModel(**transaction_data.model_dump())
            self.db.add(new_transaction)
            self.db.commit()
            return JSONResponse(content=jsonable_encoder(new_transaction), status_code=201)
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    def get_all(self):
        transactions = self.db.query(TransactionModel).all()
        return JSONResponse(content=jsonable_encoder(transactions), status_code=200)

    def get_by_user(self, user_id: int):
        transactions = self.db.query(TransactionModel).options(
            joinedload(TransactionModel.account),
            joinedload(TransactionModel.category),
            joinedload(TransactionModel.type)
        ).filter(TransactionModel.user_id == user_id).all()
        return JSONResponse(content=jsonable_encoder(transactions), status_code=200)

    def get_by_user_and_filter(self, user_id: int, filter: TransactionFilter):
        query = self.db.query(TransactionModel).options(
            joinedload(TransactionModel.account),
            joinedload(TransactionModel.category),
            joinedload(TransactionModel.type)
        ).filter(TransactionModel.user_id == user_id)

        if filter.account_id is not None:
            query = query.filter(
                TransactionModel.account_id == filter.account_id)
        if filter.transaction_type_id is not None:
            query = query.filter(TransactionModel.type_id ==
                                 filter.transaction_type_id)
        if filter.transaction_category_id is not None:
            query = query.filter(TransactionModel.category_id ==
                                 filter.transaction_category_id)
        if filter.start_date is not None:
            start_date = datetime.strptime(filter.start_date, '%Y-%m-%d')
            query = query.filter(TransactionModel.date >= start_date)
        if filter.end_date is not None:
            end_date = datetime.strptime(filter.end_date, '%Y-%m-%d')
            query = query.filter(TransactionModel.date <= end_date)

        return JSONResponse(content=jsonable_encoder(query.all()), status_code=200)

    def get_summary_by_date_and_type(self, user_id: int):
        try:
            results = self.db.query(
                func.date(TransactionModel.date).label('date'),
                func.sum(TransactionModel.quantity).label('total_amount'),
                TransactionModel.type_id,
                TransactionTypeModel.name.label('type_name')
            ).join(
                TransactionTypeModel, TransactionModel.type_id == TransactionTypeModel.id
            ).filter(
                TransactionModel.user_id == user_id
            ).group_by(
                func.date(TransactionModel.date),
                TransactionModel.type_id,
                TransactionTypeModel.name
            ).all()

            summary = [
                {
                    "date": result.date,
                    "total_amount": result.total_amount,
                    "type_id": result.type_id,
                    "type_name": result.type_name
                } for result in results
            ]

            return JSONResponse(content=jsonable_encoder(summary), status_code=200)

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def _check_resource_existence(self, model, resource_id, resource_name):
        if not resource_id:
            return
        try:
            self.db.query(model).filter(model.id == resource_id).one()
        except NoResultFound:
            raise HTTPException(
                status_code=404, detail=f"{resource_name} not found")
