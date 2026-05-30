from langchain_groq import ChatGroq

from app.core.config import settings

llm = ChatGroq(
    api_key=settings.GROQ_API_KEY,
    model="openai/gpt-oss-120b",
    temperature=0.7
)


async def generate_ai_response(
    messages: list
):

    response = await llm.ainvoke(
        messages
    )

    return response.content