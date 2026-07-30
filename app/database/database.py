import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.base import Base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

# --------------------------------------------------
# SQLAlchemy Engine
# --------------------------------------------------
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=False,  # Set True only for debugging
)

# --------------------------------------------------
# Session Factory
# --------------------------------------------------
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# --------------------------------------------------
# Database Dependency
# --------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()