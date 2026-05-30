import time

from app.db.session import (
    get_new_db
)

from app.services.summary_service import (
    get_session_summaries
)

from app.services.retrieval_types import (
    RetrievalResult
)


async def retrieve_summaries(
    session_id
):

    start = time.time()

    async with get_new_db() as db:

        summaries = (
            await get_session_summaries(
                db,
                session_id
            )
        )

    context=[]

    for s in summaries[-3:]:

        context.append(
            {
                "role":"system",

                "content":
                (
                    "Conversation summary: "
                    f"{s.content}"
                )
            }
        )

    return RetrievalResult(
        source="summary",

        messages=context,

        latency_ms=(
            time.time()-start
        )*1000
    )