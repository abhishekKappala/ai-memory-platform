import json

from app.services.redis_service import (
    redis_client
)

from app.core.config import settings


def get_key(
    session_id
):
    return (
        f"stm:{session_id}"
    )


def add_recent_message(
    session_id,
    role,
    content
):

    key = get_key(
        session_id
    )

    message = {
        "role": role,
        "content": content
    }

    redis_client.rpush(
        key,
        json.dumps(message)
    )

    redis_client.ltrim(
        key,
        -settings.STM_MESSAGE_LIMIT,
        -1
    )

    redis_client.expire(
        key,
        86400
    )


def get_recent_messages(
    session_id
):

    key = get_key(
        session_id
    )

    data = redis_client.lrange(
        key,
        0,
        -1
    )

    return [
        json.loads(i)
        for i in data
    ]

def stm_exists(
    session_id
):

    return redis_client.exists(
        get_key(
            session_id
        )
    )