from langchain_groq import ChatGroq

from sqlalchemy import select

from app.models.chat_session import ChatSession

from app.core.config import settings


title_llm = ChatGroq(
    api_key=settings.GROQ_API_KEY,
    model="openai/gpt-oss-120b",
    temperature=0.7
)


async def generate_title(
    first_message: str
):

    prompt = f"""
Generate chat title.

Conversation:

{first_message}
"""

    response = await title_llm.ainvoke(
        prompt
    )

    return response.content.strip()

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
        return

    session.title = title

    await db.commit()