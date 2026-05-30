import time

from app.db.session import (
    get_new_db
)

from app.services.retrieval_service import (
    retrieve_relevant_memories
)

from app.services.retrieval_types import (
    RetrievalResult
)


async def retrieve_memory(

    user_id,

    query

):

    start=time.time()

    async with get_new_db() as db:

        result = (
            await retrieve_relevant_memories(
                db,
                user_id,
                query
            )
        )
        print("QUERY")
        print(query)
        print("RETRIEVED RELEVANT MESSAGES:")
        print(result)
        print("------------------------------")

    return RetrievalResult(

        source="memory",

        messages=result,

        latency_ms=(
            time.time()-start
        )*1000
    )