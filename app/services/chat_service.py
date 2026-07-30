from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.chat_repository import ChatRepository


class ChatService:

    @staticmethod
    def create_chat(
        db: Session,
        title: str,
        user_id: int
    ):
        return ChatRepository.create_chat(
            db=db,
            title=title,
            user_id=user_id
        )

    @staticmethod
    def get_user_chats(
        db: Session,
        user_id: int
    ):
        return ChatRepository.get_user_chats(
            db=db,
            user_id=user_id
        )

    @staticmethod
    def rename_chat(
        db: Session,
        chat_id: int,
        title: str,
        user_id: int
    ):
        chat = ChatRepository.get_chat_by_id(
            db,
            chat_id
        )

        if not chat:
            raise HTTPException(
                status_code=404,
                detail="Chat not found"
            )

        if chat.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="You are not authorized to rename this chat"
            )

        return ChatRepository.update_chat_title(
            db=db,
            chat=chat,
            title=title
        )

    @staticmethod
    def delete_chat(
        db: Session,
        chat_id: int,
        user_id: int
    ):
        chat = ChatRepository.get_chat_by_id(
            db,
            chat_id
        )

        if not chat:
            raise HTTPException(
                status_code=404,
                detail="Chat not found"
            )

        if chat.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="You are not authorized to delete this chat"
            )

        ChatRepository.delete_chat(
            db,
            chat
        )

        return {
            "message": "Chat deleted successfully"
        }