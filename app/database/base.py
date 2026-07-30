from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import models AFTER Base is created
from app.models.user import User
from app.models.chat import Chat
from app.models.message import Message
from app.models.document import Document