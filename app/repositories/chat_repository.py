from sqlalchemy.orm import Session

from app.models.chat import Chat


class ChatRepository:

    @staticmethod
    def create_chat(db: Session, title: str, user_id: int):
        chat = Chat(
            title=title,
            user_id=user_id
        )

        db.add(chat)
        db.commit()
        db.refresh(chat)

        return chat

    @staticmethod
    def get_user_chats(db: Session, user_id: int):
        return (
            db.query(Chat)
            .filter(Chat.user_id == user_id)
            .order_by(Chat.created_at.desc())
            .all()
        )

    @staticmethod
    def get_chat_by_id(db: Session, chat_id: int):
        return (
            db.query(Chat)
            .filter(Chat.id == chat_id)
            .first()
        )

    @staticmethod
    def update_chat_title(
        db: Session,
        chat: Chat,
        title: str
    ):
        chat.title = title

        db.commit()
        db.refresh(chat)

        return chat

    @staticmethod
    def delete_chat(db: Session, chat: Chat):
        db.delete(chat)
        db.commit()