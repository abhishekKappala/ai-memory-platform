from sqlalchemy.future import select

from app.models.memory import Memory

from app.services.vector_service import (
    search_candidate_memories,
    generate_embedding
)

from app.services.memory_ranking_service import (
    calculate_memory_score
)

from app.services.mmr_service import (
    maximal_marginal_relevance
)


async def retrieve_relevant_memories(
    db,
    user_id: int,
    query: str
):

    candidate_results =  search_candidate_memories(
        user_id,
        query
    )

    print("=" * 50)
    print("CANDIDATE RESULTS")
    print(candidate_results)
    print("=" * 50)

    query_embedding =  generate_embedding(
        query
    )

    documents = candidate_results.get(
        "documents",
        [[]]
    )[0]

    embeddings = candidate_results.get(
        "embeddings",
        [[]]
    )[0]

    ids = candidate_results.get(
        "ids",
        [[]]
    )[0]

    candidates = []

    for doc, emb, memory_id in zip(
        documents,
        embeddings,
        ids
    ):

        candidates.append(
            {
                "memory_id": memory_id,
                "content": doc,
                "embedding": emb
            }
        )

    diverse = maximal_marginal_relevance(
        query_embedding,
        candidates
    )

    retrieved_memories = []

    for item in diverse:

        result = await db.execute(
            select(Memory).where(
                Memory.id == int(
                    item["memory_id"]
                )
            )
        )

        memory = result.scalar_one_or_none()

        if not memory:
            continue

        semantic_score = 1.0

        final_score = (
            calculate_memory_score(
                memory,
                semantic_score
            )
        )

        retrieved_memories.append(
            (
                final_score,
                memory
            )
        )

    retrieved_memories.sort(
        key=lambda x: x[0],
        reverse=True
    )

    final_memories = []

    for _, memory in retrieved_memories[:5]:

        memory.retrieval_count += 1

        final_memories.append(
            {
                "role": "system",
                "content":
                f"Relevant memory: {memory.content}"
            }
        )

    await db.commit()

    return final_memories