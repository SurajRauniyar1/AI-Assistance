from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class ChatCreate(BaseModel):
    title: str


class ChatUpdate(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=100
    )


class ChatResponse(BaseModel):
    id: int
    title: str
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)