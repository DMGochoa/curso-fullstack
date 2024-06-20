from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.transaction_type import transaction_type_router
from routers.transaction import transaction_router
from middlewares.error_handler import ErrorHandler
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
app.add_middleware(ErrorHandler)

app.include_router(transaction_type_router)
app.include_router(transaction_router)
Base.metadata.create_all(bind=engine)
