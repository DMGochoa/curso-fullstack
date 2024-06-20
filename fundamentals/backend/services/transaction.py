from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas.transaction import Transaction
from schemas.transaction import TransactionFilter
from models.transaction_type import TransactionType as TransactionTypeModel
from models.transaction import Transaction as TransactionModel
from config.database import Session


class TransactionService:
    def __init__(self):
        self.db = Session()

    def create(self, transaction_data: Transaction):
        try:
            self._check_resource_existence(
                TransactionTypeModel,
                transaction_data.type_id,
                "Transaction type"
            )
            new_transaction = TransactionModel(**transaction_data.model_dump())
            self.db.add(new_transaction)
            self.db.commit()
            return JSONResponse(
                content=jsonable_encoder(new_transaction),
                status_code=201
            )
        except:
            raise HTTPException(
                status_code=404,
                detail=f"Transaction type not found"
            )

    def update(self, transaction_id: int, transaction_data: Transaction):
        try:
            self._check_resource_existence(
                TransactionModel,
                transaction_id,
                "Transaction"
            )
            self._check_resource_existence(
                TransactionTypeModel,
                transaction_data.type_id,
                "Transaction type"
            )
            self.db.query(TransactionModel).filter(TransactionModel.id == transaction_id).update(
                transaction_data.model_dump()
            )
            self.db.commit()
            return JSONResponse(
                content=jsonable_encoder(transaction_data),
                status_code=200
            )
        except:
            raise HTTPException(
                status_code=404,
                detail="Transaction not found"
            )

    def get_all(self):
        transactions = self.db.query(TransactionModel).options(
            joinedload(TransactionModel.type),
        ).all()
        return JSONResponse(
            content=jsonable_encoder(transactions),
            status_code=200
        )

    def get_some(self, limit: int, offset: int):
        transactions = self.db.query(TransactionModel).options(
            joinedload(TransactionModel.type),
        ).limit(limit).offset(offset).all()
        return JSONResponse(
            content=jsonable_encoder(transactions),
            status_code=200
        )

    def get_by_id(self, transaction_id: int):
        transaction = self.db.query(TransactionModel).options(
            joinedload(TransactionModel.type),
        ).filter(TransactionModel.id == transaction_id).first()
        if not transaction:
            raise HTTPException(
                status_code=404,
                detail="Transaction not found"
            )
        return JSONResponse(
            content=jsonable_encoder(transaction),
            status_code=200
        )

    def get_unique_accounts(self):
        accounts = self.db.query(TransactionModel.account).options(
            joinedload(TransactionModel.type),
        ).distinct().all()
        return JSONResponse(
            content=jsonable_encoder(accounts),
            status_code=200
        )

    def get_unique_categories(self):
        categories = self.db.query(TransactionModel.category).options(
            joinedload(TransactionModel.type),
        ).distinct().all()
        return JSONResponse(
            content=jsonable_encoder(categories),
            status_code=200
        )

    def get_summary_by_date_and_type(self):
        transactions = self.db.query(
            func.date(TransactionModel.date).label('date'),
            TransactionTypeModel.name,
            func.sum(TransactionModel.quantity).label('total_amount')
        ).join(
            TransactionTypeModel,
            TransactionModel.type_id == TransactionTypeModel.id
        ).group_by(
            func.date(TransactionModel.date),
            TransactionTypeModel.name
        ).order_by(
            func.date(TransactionModel.date).desc()
        ).all()

        summary = [
            {
                "date": result.date,
                "type": result.name,
                "total_amount": result.total_amount
            } for result in transactions
        ]

        return JSONResponse(
            content=jsonable_encoder(summary),
            status_code=200
        )

    def get_summary_total_amount_by_type(self):
        total_amount = self.db.query(func.sum(TransactionModel.quantity)).scalar()
        transactions = self.db.query(
            TransactionTypeModel.name,
            func.sum(TransactionModel.quantity).label('total_amount')
        ).join(
            TransactionModel
        ).group_by(
            TransactionTypeModel.name
        ).all()

        summary = [
            {
                "type": result.name,
                "total_amount": result.total_amount,
                "percentage": round((result.total_amount * 100) / total_amount, 2)
            } for result in transactions
        ]

        return JSONResponse(
            content=jsonable_encoder(summary),
            status_code=200
        )
    
    def get_summary_avg_amount_monthly_by_type(self):
        try:
            # Obtener la suma de cantidades agrupadas por tipo y por mes
            monthly_sums = self.db.query(
                TransactionTypeModel.name,
                func.extract('year', TransactionModel.date).label('year'),
                func.extract('month', TransactionModel.date).label('month'),
                func.sum(TransactionModel.quantity).label('total_amount')
            ).join(
                TransactionTypeModel,
                TransactionModel.type_id == TransactionTypeModel.id
            ).group_by(
                TransactionTypeModel.name,
                func.extract('year', TransactionModel.date),
                func.extract('month', TransactionModel.date)
            ).all()

            # Calcular el promedio mensual por tipo
            type_monthly_totals = {}
            for record in monthly_sums:
                type_name = record.name
                if type_name not in type_monthly_totals:
                    type_monthly_totals[type_name] = []
                type_monthly_totals[type_name].append(record.total_amount)

            type_monthly_averages = [
                {
                    "type": type_name,
                    "average_monthly_amount": sum(amounts) / len(amounts)
                }
                for type_name, amounts in type_monthly_totals.items()
            ]

            return JSONResponse(
                content=jsonable_encoder(type_monthly_averages),
                status_code=200
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )

    def _check_resource_existence(self, model, resource_id, resource_name):
        if not resource_id:
            return
        try:
            all_ids = self.db.query(model).filter(
                model.id == resource_id).first()
            if not all_ids:
                raise NoResultFound
        except NoResultFound:
            raise HTTPException(
                status_code=404, detail=f"{resource_name} not found")
