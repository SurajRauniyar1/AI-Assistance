from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@router.get("/me")
def current_user(
    user=Depends(get_current_user),
):
    return {
        "id": user.id,
        "name": user.full_name,
        "email": user.email,
    }