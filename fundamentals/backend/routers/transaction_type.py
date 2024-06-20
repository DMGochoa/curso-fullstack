from fastapi import APIRouter, Depends, Request
from services.transaction_type import TransactionTypeService
from schemas.transaction_type import TransactionType

transaction_type_router = APIRouter(
    prefix="/transactions_types",
    tags=["transactions"]
)

@transaction_type_router.post("", response_model=TransactionType)
def create_transaction_type(request: Request, transaction_type: TransactionType):
    service = TransactionTypeService()
    result = service.create(transaction_type)
    del service
    return result

@transaction_type_router.get("", response_model=list[TransactionType])
def get_transaction_types():
    service = TransactionTypeService()
    result = service.get_all()
    del service
    return result

@transaction_type_router.put("/{transaction_type_id}", response_model=TransactionType)
def update_transaction_type(request: Request, transaction_type_id: int, transaction_type: TransactionType):
    service = TransactionTypeService()
    result = service.update(transaction_type_id, transaction_type)
    del service
    return result

@transaction_type_router.get("/{transaction_type_id}", response_model=TransactionType)
def get_transaction_type(transaction_type_id: int):
    service = TransactionTypeService()
    result = service.get(transaction_type_id)
    del service
    return result

@transaction_type_router.get("/", response_model=list[TransactionType])
def get_by_limit_and_offset(limit: int, offset: int):
    service = TransactionTypeService()
    result = service.get_some(limit, offset)
    del service
    return result

@transaction_type_router.delete("/{transaction_type_id}")
def delete_transaction_type(transaction_type_id: int):
    service = TransactionTypeService()
    result = service.delete(transaction_type_id)
    del service
    return result
