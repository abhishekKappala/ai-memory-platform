from sqlalchemy import *

from datetime import datetime

from app.db.database import Base


class Metric(
    Base
):

    __tablename__="metrics"

    id=Column(
        Integer,
        primary_key=True
    )

    endpoint=Column(
        String
    )

    latency_ms=Column(
        Float
    )

    input_tokens=Column(
        Integer
    )

    output_tokens=Column(
        Integer
    )

    retrieval_count=Column(
        Integer
    )

    created_at=Column(
        DateTime,
        default=datetime.utcnow
    )