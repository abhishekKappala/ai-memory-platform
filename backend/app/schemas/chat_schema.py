from pydantic import BaseModel
from datetime import datetime


class ChatSessionCreate(BaseModel):
    title: str


class ChatSessionResponse(BaseModel):

    id: int
    title: str
    created_at: datetime

    class Config:
        from_attributes = True


class MessageCreate(BaseModel):
    content: str


class MessageResponse(BaseModel):

    id: int
    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True