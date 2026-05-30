from app.services.llm_service import llm


async def llm_stream_node(
    state
):
    async for chunk in llm.astream(
        state["context"]
    ):
        yield chunk.content