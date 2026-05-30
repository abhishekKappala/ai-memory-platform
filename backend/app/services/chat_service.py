from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.chat_session import ChatSession
from app.models.message import Message

from app.models.chat_session import (
    ChatSession
)

async def create_chat_session(
    db: AsyncSession,
    title: str,
    user_id: int
):

    session = ChatSession(
        title=title,
        user_id=user_id
    )

    db.add(session)

    await db.commit()

    await db.refresh(session)

    return session


async def create_message(
    db: AsyncSession,
    session_id: int,
    role: str,
    content: str,
):

    message = Message(
        session_id=session_id,
        role=role,
        content=content
    )

    db.add(message)

    await db.commit()

    await db.refresh(message)

    return message


async def get_session_messages(
    db: AsyncSession,
    session_id: int
):

    result = await db.execute(
        select(Message)
        .where(Message.session_id == session_id)
        .order_by(Message.created_at)
    )

    return result.scalars().all()

# 2...........................................

async def create_assistant_message(
    db: AsyncSession,
    session_id: int,
    content: str,
):

    message = Message(
        session_id=session_id,
        role="assistant",
        content=content
    )

    db.add(message)

    await db.commit()

    await db.refresh(message)

    return message

async def get_session(
    db,
    session_id
):

    result = await db.execute(

        select(
            ChatSession
        ).where(

            ChatSession.id
            ==
            session_id

        )

    )

    return (
        result.scalar_one_or_none()
    )

async def get_user_sessions(
    db,
    user_id
):

    result = await db.execute(

        select(ChatSession)

        .where(
            ChatSession.user_id == user_id
        )

        .order_by(
            ChatSession.created_at.desc()
        )

    )

    return result.scalars().all()

async def update_session_title(
    db,
    session_id: int,
    title: str
):

    result = await db.execute(
        select(ChatSession)
        .where(
            ChatSession.id == session_id
        )
    )

    session = result.scalar_one_or_none()

    if not session:
        return None

    session.title = title

    await db.commit()

    await db.refresh(session)

    return session