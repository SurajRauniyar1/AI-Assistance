from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.chat_repository import ChatRepository
from app.repositories.message_repository import MessageRepository


class MessageService:

    @staticmethod
    def send_message(db: Session, chat_id: int, user_id: int, content: str):

        chat = ChatRepository.get_chat_by_id(db, chat_id)

        if not chat:
            raise HTTPException(
                status_code=404,
                detail="Chat not found"
            )

        if chat.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="You are not authorized to access this chat"
            )

        return MessageRepository.create_message(
            db=db,
            chat_id=chat_id,
            role="user",
            content=content
        )

    @staticmethod
    def get_chat_history(db: Session, chat_id: int, user_id: int):

        chat = ChatRepository.get_chat_by_id(db, chat_id)

        if not chat:
            raise HTTPException(
                status_code=404,
                detail="Chat not found"
            )

        if chat.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="You are not authorized to access this chat"
            )

        return MessageRepository.get_chat_messages(
            db=db,
            chat_id=chat_id
        )