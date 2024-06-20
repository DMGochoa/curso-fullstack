from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas.transaction_type import TransactionType
from models.transaction_type import TransactionType as TransactionTypeModel
from config.database import Session

transaction_type_router = APIRouter()
base_path = "/transaction_types"


@transaction_type_router.post(base_path)
def create_transaction_type(transaction_type: TransactionType):
    db = Session()
    new_transaction_type = TransactionTypeModel(
        **transaction_type.model_dump())
    db.add(new_transaction_type)
    db.commit()
    return JSONResponse(content={"message": "Transaction type created successfully"}, status_code=201)


@transaction_type_router.get(base_path)
def get_transaction_types():
    db = Session()
    transaction_types = db.query(TransactionTypeModel).all()
    data = jsonable_encoder(transaction_types)
    return JSONResponse(content=data, status_code=200)


@transaction_type_router.get(base_path + "/user/{user_id}")
def get_user_transaction_types(user_id: int):
    db = Session()
    transaction_types = db.query(TransactionTypeModel).filter(
        TransactionTypeModel.user_id == user_id).all()
    data = jsonable_encoder(transaction_types)
    return JSONResponse(content=data, status_code=200)


@transaction_type_router.delete(base_path + "/{id}")
def delete_transaction_type(id: int):
    db = Session()
    db.query(TransactionTypeModel).filter(
        TransactionTypeModel.id == id).delete()
    db.commit()
    return JSONResponse(content={"message": "Transaction type deleted successfully"}, status_code=200)


@transaction_type_router.put(base_path + "/{id}")
def update_transaction_type(id: int, transaction_type: TransactionType):
    db = Session()
    transaction_type_data = transaction_type.model_dump()
    db.query(TransactionTypeModel).filter(
        TransactionTypeModel.id == id).update(transaction_type_data)
    db.commit()
    return JSONResponse(content={"message": "Transaction type updated successfully"}, status_code=200)
