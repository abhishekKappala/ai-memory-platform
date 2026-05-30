from langchain_groq import ChatGroq

from app.core.config import settings
from app.services.prompt_service import (
    load_system_prompt
)

# summary_llm = ChatGroq(
#     api_key=settings.GROQ_API_KEY,
#     model="llama3-8b-8192",
#     temperature=0.2
# )

summary_llm = ChatGroq(
    api_key=settings.GROQ_API_KEY,
    model="openai/gpt-oss-120b",
    temperature=0.7
)

# ######################################################################################
# summarization prompt is not been used
# ######################################################################################

async def generate_summary(
    conversation_text: str
):

    prompt = f"""
Summarize this conversation:

{conversation_text}
"""

    response = await summary_llm.ainvoke(
        prompt
    )

    return response.content