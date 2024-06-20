from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer

from schemas.account import Account
from models.account import Account as AccountModel
from config.database import Session

account_router = APIRouter()
base_path = "/accounts"


@account_router.post(base_path)
def create_account(account: Account):
    db = Session()
    new_account = AccountModel(**account.model_dump())
    db.add(new_account)
    db.commit()
    return JSONResponse(content={"message": "Account created successfully"}, status_code=201)


@account_router.get(base_path)
def get_accounts():
    db = Session()
    accounts = db.query(AccountModel).all()
    data = jsonable_encoder(accounts)
    return JSONResponse(content=data, status_code=200)


@account_router.get(base_path + "/user", dependencies=[Depends(JWTBearer())])
def get_user_accounts(request: Request):
    user_id = request.state.user_id
    db = Session()
    accounts = db.query(AccountModel).filter(
        AccountModel.user_id == user_id).all()
    data = jsonable_encoder(accounts)
    return JSONResponse(content=data, status_code=200)


@account_router.delete(base_path + "/{id}")
def delete_account(id: int):
    db = Session()
    db.query(AccountModel).filter(AccountModel.id == id).delete()
    db.commit()
    return JSONResponse(content={"message": "Account deleted successfully"}, status_code=200)


@account_router.put(base_path + "/{id}")
def update_account(id: int, account: Account):
    db = Session()
    account_data = account.model_dump()
    db.query(AccountModel).filter(AccountModel.id == id).update(account_data)
    db.commit()
    return JSONResponse(content={"message": "Account updated successfully"}, status_code=200)
