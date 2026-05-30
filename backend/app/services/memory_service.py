from sqlalchemy.ext.asyncio import AsyncSession

from app.models.memory import Memory

from sqlalchemy.future import select

from app.services.vector_service import (
    store_memory_embedding
)

from sqlalchemy.future import select

from app.services.memory_dedup_service import (
    is_duplicate_memory
)



async def create_memory(
    db: AsyncSession,
    user_id: int,
    memory_data: dict
):

    # ---------------------------------------------------------
    existing_memories = await db.execute(
        select(Memory).where(
            Memory.user_id == user_id
        )
    )

    existing_memories = (
        existing_memories.scalars().all()
    )

    for existing_memory in existing_memories:

        if is_duplicate_memory(
            existing_memory.content,
            memory_data.get("content", "")
        ):
            return existing_memory

    # ---------------------------------------------------------------

    print("MEMORY USER:")
    print(user_id)
    memory = Memory(
        user_id=user_id,

        category=memory_data.get(
            "category",
            "general"
        ),

        content=memory_data.get(
            "content",
            ""
        ),

        importance_score=memory_data.get(
            "importance_score",
            0.5
        ),

        confidence_score=memory_data.get(
            "confidence_score",
            0.5
        )
    )

    db.add(memory)

    await db.commit()

    await db.refresh(memory)

    store_memory_embedding(
        memory.id,
        user_id,
        memory.content
    )

    return memory




async def get_user_memories(
    db,
    user_id
):

    result = await db.execute(
        select(Memory)
        .where(Memory.user_id == user_id)
        .order_by(
            Memory.importance_score.desc()
        )
    )


    return result.scalars().all()

