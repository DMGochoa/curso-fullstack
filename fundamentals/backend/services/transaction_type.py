from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.database import Session
from schemas.transaction_type import TransactionType
from models.transaction_type import TransactionType as TransactionTypeModel

class TransactionTypeService:
    def __init__(self):
        self.db = Session()

    def create(self, transaction_type_data: TransactionType):
        new_transaction_type = TransactionTypeModel(**transaction_type_data.model_dump())
        self.db.add(new_transaction_type)
        self.db.commit()
        return JSONResponse(
            content={
                "message": "Transaction type created",
                }, 
            status_code=201
        )

    def get_all(self):
        transaction_types = self.db.query(TransactionTypeModel).all()
        return JSONResponse(
            content=jsonable_encoder(transaction_types), 
            status_code=200
        )

    def get(self, transaction_type_id: int):
        try:
            transaction_type = self.db.query(TransactionTypeModel).filter(
                TransactionTypeModel.id == transaction_type_id
                ).first()
            return JSONResponse(
                content=jsonable_encoder(transaction_type), 
                status_code=200
            )
        except NoResultFound:
            raise HTTPException(
                status_code=404, 
                detail="Transaction type not found"
            )

    def get_some(self, limit: int, offset: int):
        transaction_types = self.db.query(TransactionTypeModel).limit(limit).offset(offset).all()
        return JSONResponse(
            content=jsonable_encoder(transaction_types), 
            status_code=200
        )

    def update(self, transaction_type_id: int, transaction_type_data: TransactionType):
        try:
            self._check_resource_existence(
                TransactionTypeModel, 
                transaction_type_id, 
                "Transaction type"
            )
            self.db.query(TransactionTypeModel).filter(TransactionTypeModel.id == transaction_type_id).first().update(
                transaction_type_data.model_dump()
            )
            self.db.commit()
            return JSONResponse(
                content={
                    "message": "Transaction type updated"
                    },
                status_code=200
            )
        except:
            raise HTTPException(
                status_code=404, 
                detail="Transaction type not found"
            )

    def _check_resource_existence(self, model, resource_id, resource_name):
        try:
            self.db.query(model).filter(model.id == resource_id).one()
        except NoResultFound:
            raise HTTPException(
                status_code=404, 
                detail=f"{resource_name} not found"
            )

    def delete(self, transaction_type_id: int):
        try:
            self._check_resource_existence(
                TransactionTypeModel, 
                transaction_type_id, 
                "Transaction type"
            )
            self.db.query(TransactionTypeModel).filter(TransactionTypeModel.id == transaction_type_id).delete()
            self.db.commit()
            return JSONResponse(
                content=jsonable_encoder({
                    "message": f"Transaction type deleted with id {transaction_type_id}"
                    }), 
                status_code=200
            )
        except:
            raise HTTPException(
                status_code=404, 
                detail="Transaction type not found"
            )
