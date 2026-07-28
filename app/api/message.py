from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User
from app.schemas.message import MessageCreate, MessageResponse
from app.services.message_service import MessageService

router = APIRouter(
    prefix="/message",
    tags=["Message"]
)


@router.post("/send/{chat_id}", response_model=MessageResponse)
def send_message(
    chat_id: int,
    message: MessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return MessageService.send_message(
        db=db,
        chat_id=chat_id,
        user_id=current_user.id,
        content=message.content
    )


@router.get("/history/{chat_id}", response_model=List[MessageResponse])
def get_chat_history(
    chat_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return MessageService.get_chat_history(
        db=db,
        chat_id=chat_id,
        user_id=current_user.id
    )