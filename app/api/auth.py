from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.hashing import verify_password
from app.auth.jwt_handler import create_access_token
from app.database.database import get_db
from app.repositories.user import get_user_by_email
from app.schemas.user import UserRegister, UserResponse
from app.services.user import register_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201,
)
def register(
    request: UserRegister,
    db: Session = Depends(get_db),
):
    user = register_user(db, request)

    if user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already exists",
        )

    return user


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = get_user_by_email(db, form_data.username)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    if not verify_password(
        form_data.password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    token = create_access_token(
        {
            "sub": user.email,
            "id": user.id,
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }