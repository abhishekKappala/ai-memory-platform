from langchain_groq import ChatGroq


llm = ChatGroq(
    
    api_key=settings.GROQ_API_KEY,
    
    model="openai/gpt-oss-120b",

    temperature=0.7,

    streaming=True
)

async def stream_response(

    messages
):

    async for chunk in llm.astream(
        messages
    ):

        if chunk.content:

            yield chunk.content