from app.auth.hashing import hash_password
from app.models.user import User
from app.repositories.user import (
    create_user,
    get_user_by_email,
)


def register_user(db, request):

    existing = get_user_by_email(
        db,
        request.email
    )

    if existing:
        return None

    user = User(
        full_name=request.full_name,
        email=request.email,
        hashed_password=hash_password(request.password)
    )

    return create_user(db, user)