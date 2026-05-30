from sqlalchemy import *

from datetime import datetime

from app.db.database import Base


class Evaluation(
    Base
):

    __tablename__="evaluations"

    id=Column(
        Integer,
        primary_key=True
    )

    query=Column(
        Text
    )

    response=Column(
        Text
    )

    score=Column(
        Float
    )

    created_at=Column(
        DateTime,
        default=datetime.utcnow
    )