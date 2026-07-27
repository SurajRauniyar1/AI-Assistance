from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.user import router as user_router

from app.api.root import router as root_router
from app.database.database import engine
from app.database.base import Base

# Import all models here
from app.models.user import User
from app.api import chat


Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Developer Assistant")

app.include_router(root_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(chat.router)