from fastapi import APIRouter, Depends, Request
from services.transaction import TransactionService
from schemas.transaction import Transaction, TransactionFilter

transaction_router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@transaction_router.post("", response_model=Transaction)
def create_transaction(request: Request, transaction: Transaction):
    service = TransactionService()
    result = service.create(transaction)
    del service
    return result

@transaction_router.get("", response_model=list[Transaction])
def get_transactions():
    service = TransactionService()
    result = service.get_all()
    del service
    return result

@transaction_router.get("/", response_model=list[Transaction])
def get_by_limit_and_offset(limit: int, offset: int):
    service = TransactionService()
    result = service.get_some(limit, offset)
    del service
    return result

@transaction_router.get("/summary", response_model=list[Transaction])
def get_summary_by_date_and_type():
    service = TransactionService()
    result = service.get_summary_by_date_and_type()
    del service
    return result

@transaction_router.get("/summary/average-monthly", response_model=list[Transaction])
def get_average_monthly_transaction():
    service = TransactionService()
    result = service.get_summary_avg_amount_monthly_by_type()
    del service
    return result

@transaction_router.get("/summary/type/total", response_model=list[Transaction])
def get_summary_total_amount_by_type():
    service = TransactionService()
    result = service.get_summary_total_amount_by_type()
    del service
    return result

@transaction_router.put("/{transaction_id}", response_model=Transaction)
def update_transaction(request: Request, transaction_id: int, transaction: Transaction):
    service = TransactionService()
    result = service.update(transaction_id, transaction)
    del service
    return result

@transaction_router.get("/{transaction_id}", response_model=Transaction)
def get_transaction(transaction_id: int):
    service = TransactionService()
    result = service.get(transaction_id)
    del service
    return result
