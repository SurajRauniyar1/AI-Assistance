from fastapi import HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.repositories.chat_repository import ChatRepository
from app.repositories.message_repository import MessageRepository

from app.ai.prompt_builder import build_messages
from app.ai.groq_client import (
    get_ai_response,
    stream_ai_response,
)
from app.ai.retriever import get_context
from app.ai.title_generator import generate_chat_title


class MessageService:

    @staticmethod
    def generate_title_if_needed(
        db: Session,
        chat
    ):
        # Generate title only once
        if chat.title != "New Chat":
            return

        messages = MessageRepository.get_chat_messages(
            db,
            chat.id
        )

        user_messages = [
            m for m in messages
            if m.role == "user"
        ]

        # Only after the very first user message
        if len(user_messages) != 1:
            return

        title = generate_chat_title(
            user_messages[0].content
        )

        ChatRepository.update_chat_title(
            db=db,
            chat=chat,
            title=title
        )

    @staticmethod
    def send_message(
        db: Session,
        chat_id: int,
        content: str,
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
                detail="Not authorized"
            )

        # Save user message
        MessageRepository.create_message(
            db=db,
            chat_id=chat_id,
            role="user",
            content=content
        )

        # Generate title if needed
        MessageService.generate_title_if_needed(
            db,
            chat
        )

        # Conversation history
        history = MessageRepository.get_messages_for_ai(
            db,
            chat_id
        )

        # Retrieve document context
        context = get_context(content)

        # Build prompt
        messages = build_messages(
            history,
            context=context
        )

        # AI response
        ai_response = get_ai_response(messages)

        # Save assistant message
        assistant_message = MessageRepository.create_message(
            db=db,
            chat_id=chat_id,
            role="assistant",
            content=ai_response
        )

        return assistant_message

    @staticmethod
    def stream_message(
        db: Session,
        chat_id: int,
        content: str,
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
                detail="Not authorized"
            )

        # Save user message
        MessageRepository.create_message(
            db=db,
            chat_id=chat_id,
            role="user",
            content=content
        )

        # Generate title if needed
        MessageService.generate_title_if_needed(
            db,
            chat
        )

        # Conversation history
        history = MessageRepository.get_messages_for_ai(
            db,
            chat_id
        )

        # Retrieve document context
        context = get_context(content)

        # Build prompt
        messages = build_messages(
            history,
            context=context
        )

        def generate():

            full_response = ""

            for token in stream_ai_response(messages):
                full_response += token
                yield token

            MessageRepository.create_message(
                db=db,
                chat_id=chat_id,
                role="assistant",
                content=full_response
            )

        return StreamingResponse(
            generate(),
            media_type="text/plain"
        )

    @staticmethod
    def get_chat_history(
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
                detail="Not authorized"
            )

        return MessageRepository.get_chat_messages(
            db,
            chat_id
        )