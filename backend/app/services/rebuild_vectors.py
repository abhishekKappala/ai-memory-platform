import asyncio

from sqlalchemy import select

from app.db.session import AsyncSessionLocal

from app.models.memory import Memory

from app.services.vector_service import (
    store_memory_embedding
)


async def main():

    async with AsyncSessionLocal() as db:

        result = await db.execute(
            select(Memory)
        )

        memories = (
            result.scalars().all()
        )

        print(
            f"Found {len(memories)} memories"
        )

        for memory in memories:

            store_memory_embedding(
                memory.id,
                memory.user_id,
                memory.content
            )

            print(
                f"Stored memory {memory.id}"
            )


asyncio.run(main())