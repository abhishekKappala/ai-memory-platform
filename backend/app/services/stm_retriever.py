import time

from app.services.stm_service import (
    get_recent_messages
)

from app.services.retrieval_types import (
    RetrievalResult
)


async def retrieve_stm(
    session_id
):

    start = time.time()

    messages = get_recent_messages(
        session_id
    )

    return RetrievalResult(
        source="stm",
        messages=messages,
        latency_ms=(
            time.time()-start
        )*1000
    )