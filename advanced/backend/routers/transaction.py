from fastapi import APIRouter, Depends, Request
from services.transaction import TransactionService
from schemas.transaction import Transaction, TransactionFilter
from middlewares.jwt_bearer import JWTBearer

transaction_router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    dependencies=[Depends(JWTBearer())]
)

@transaction_router.post("/", response_model=Transaction)
def create_transaction(request: Request, transaction: Transaction):
    user_id = request.state.user_id
    transaction.user_id = user_id
    service = TransactionService()
    return service.create(transaction)

@transaction_router.get("/", response_model=list[Transaction])
def get_transactions(request: Request):
    user_id = request.state.user_id
    service = TransactionService()
    return service.get_by_user(user_id)

@transaction_router.post("/filter", response_model=list[Transaction])
def get_transactions_by_filter(request: Request, filter: TransactionFilter):
    user_id = request.state.user_id
    service = TransactionService()
    return service.get_by_user_and_filter(user_id, filter)

@transaction_router.get("/summary", response_model=list[dict])
def get_transaction_summary(request: Request):
    user_id = request.state.user_id
    service = TransactionService()
    return service.get_summary_by_date_and_type(user_id)


