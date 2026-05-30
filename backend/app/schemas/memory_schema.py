from pydantic import BaseModel
from datetime import datetime


class MemoryResponse(BaseModel):

    id: int
    category: str
    content: str

    importance_score: float
    confidence_score: float

    retrieval_count: int

    created_at: datetime

    class Config:
        from_attributes = True