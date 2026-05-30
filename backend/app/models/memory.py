from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import Text

from datetime import datetime

from app.db.database import Base


class Memory(Base):

    __tablename__ = "memories"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    category = Column(
        String,
        nullable=False
    )

    content = Column(
        Text,
        nullable=False
    )

    importance_score = Column(
        Float,
        default=0.5
    )

    confidence_score = Column(
        Float,
        default=0.5
    )

    retrieval_count = Column(
        Integer,
        default=0
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    last_accessed_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    decay_score = Column(
        Float,
        default=1.0
    )

