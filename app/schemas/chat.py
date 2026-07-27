from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ChatCreate(BaseModel):
    title: str


class ChatResponse(BaseModel):
    id: int
    title: str
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)