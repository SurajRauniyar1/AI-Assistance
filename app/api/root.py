from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    """
    Root endpoint of our application.
    """

    return {
        "status": "success",
        "message": "Welcome to AI Developer Assistant 🚀",
        "version": "1.0.0"
    }