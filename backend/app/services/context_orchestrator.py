import asyncio

from app.services.stm_retriever import (
    retrieve_stm
)

from app.services.summary_retriever import (
    retrieve_summaries
)

from app.services.memory_retriever import (
    retrieve_memory
)

from app.services.prompt_service import (
    load_system_prompt
)


async def build_context(
    db,
    session_id,
    user_id,
    query
):

    stm_task = retrieve_stm(
        session_id
    )

    summary_task = retrieve_summaries(
        session_id
    )

    memory_task = retrieve_memory(
        user_id,
        query
    )

    stm, summaries, memories = (
        await asyncio.gather(
            stm_task,
            summary_task,
            memory_task
        )
    )

    return [

        {
            "role":"system",

            "content":
            load_system_prompt()
        },

        *memories.messages,

        *summaries.messages,

        *stm.messages
    ]