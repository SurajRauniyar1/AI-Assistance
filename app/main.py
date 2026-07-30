from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.root import router as root_router
from app.api.auth import router as auth_router
from app.api.user import router as user_router
from app.api.health import router as health_router
from app.api import chat
from app.api import message
from app.api import document


# --------------------------------------------------
# Application Lifespan
# --------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting AI Developer Assistant Backend...")
    # Future startup tasks:
    # - Initialize ChromaDB
    # - Load ML models
    # - Warm caches
    yield
    print("🛑 Shutting down AI Developer Assistant Backend...")


# --------------------------------------------------
# FastAPI App
# --------------------------------------------------
app = FastAPI(
    title="AI Developer Assistant",
    description="Backend API for AI Developer Assistant",
    version="1.0.0",
    lifespan=lifespan,
)


# --------------------------------------------------
# CORS Configuration
# --------------------------------------------------
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Routers
# --------------------------------------------------
app.include_router(root_router)
app.include_router(health_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(chat.router)
app.include_router(message.router)
app.include_router(document.router)