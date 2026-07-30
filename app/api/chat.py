from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.database import get_db
from app.schemas.chat import (
    ChatCreate,
    ChatUpdate,
    ChatResponse,
)
from app.services.chat_service import ChatService
from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/create", response_model=ChatResponse)
def create_chat(
    chat: ChatCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return ChatService.create_chat(
        db=db,
        title=chat.title,
        user_id=current_user.id
    )


@router.get("/list", response_model=List[ChatResponse])
def list_chats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return ChatService.get_user_chats(
        db=db,
        user_id=current_user.id
    )


@router.patch("/{chat_id}", response_model=ChatResponse)
def rename_chat(
    chat_id: int,
    chat: ChatUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return ChatService.rename_chat(
        db=db,
        chat_id=chat_id,
        title=chat.title,
        user_id=current_user.id
    )


@router.delete("/{chat_id}")
def delete_chat(
    chat_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return ChatService.delete_chat(
        db=db,
        chat_id=chat_id,
        user_id=current_user.id
    )