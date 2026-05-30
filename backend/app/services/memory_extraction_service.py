import json

from langchain_groq import ChatGroq

from app.core.config import settings

memory_llm = ChatGroq(
    api_key=settings.GROQ_API_KEY,
    model="openai/gpt-oss-120b",
    temperature=0
)


async def extract_memories(
    conversation_text: str
):

    prompt = f"""
Extract ONLY long-term useful memories.

Store:
- preferences
- goals
- recurring projects
- interests
- personal profile details
- behavioral patterns

Ignore:
- temporary statements
- greetings
- filler discussion
- one-time casual messages

Return structured JSON.

Each memory must contain:
- category
- content
- importance_score
- confidence_score

Example Format:
[
{{
    "category": "Work",
    "content": "Completed the Q3 financial report.",
    "importance_score": 4,
    "confidence_score": 0.95
}}
]
User messages:
{conversation_text}
"""

#     prompt = f"""
# Extract long-term useful memories.

# Return JSON list.

# Conversation:

# {conversation_text}
# """


    response = await memory_llm.ainvoke(
        prompt
    )

    try:
        return json.loads(response.content)
    
    except Exception as e:

        return []