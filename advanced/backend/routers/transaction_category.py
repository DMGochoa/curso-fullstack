from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas.transaction_category import TransactionCategory
from models.transaction_category import TransactionCategory as TransactionCategoryModel
from config.database import Session

transaction_category_router = APIRouter()
base_path = "/transaction_categories"

@transaction_category_router.post(base_path)
def create_transaction_category(transaction_category: TransactionCategory):
    db = Session()
    new_transaction_category = TransactionCategoryModel(**transaction_category.model_dump())
    db.add(new_transaction_category)
    db.commit()
    return JSONResponse(content={"message": "Transaction category created successfully"}, status_code=201)

@transaction_category_router.get(base_path)
def get_transaction_categories():
    db = Session()
    transaction_categories = db.query(TransactionCategoryModel).all()
    data = jsonable_encoder(transaction_categories)
    return JSONResponse(content=data, status_code=200)

@transaction_category_router.get(base_path + "/user/{user_id}")
def get_user_transaction_categories(user_id: int):
    db = Session()
    transaction_categories = db.query(TransactionCategoryModel).filter(TransactionCategoryModel.user_id == user_id).all()
    data = jsonable_encoder(transaction_categories)
    return JSONResponse(content=data, status_code=200)

@transaction_category_router.delete(base_path + "/{id}")
def delete_transaction_category(id: int):
    db = Session()
    db.query(TransactionCategoryModel).filter(TransactionCategoryModel.id == id).delete()
    db.commit()
    return JSONResponse(content={"message": "Transaction category deleted successfully"}, status_code=200)

@transaction_category_router.put(base_path + "/{id}")
def update_transaction_category(id: int, transaction_category: TransactionCategory):
    db = Session()
    transaction_category_data = transaction_category.model_dump()
    db.query(TransactionCategoryModel).filter(TransactionCategoryModel.id == id).update(transaction_category_data)
    db.commit()
    return JSONResponse(content={"message": "Transaction category updated successfully"}, status_code=200)
