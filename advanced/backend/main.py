from fastapi import FastAPI
from routers.auth import auth_router
from routers.user import user_router
from routers.account import account_router
from routers.transaction import transaction_router
from routers.transaction_type import transaction_type_router
from routers.transaction_category import transaction_category_router
from fastapi.middleware.cors import CORSMiddleware
from config.database import engine, Base


app = FastAPI()
app.title = "Money Tracker API"
app.version = "0.1.0"

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(account_router)
app.include_router(transaction_router)
app.include_router(transaction_type_router)
app.include_router(transaction_category_router)
Base.metadata.create_all(bind=engine)
