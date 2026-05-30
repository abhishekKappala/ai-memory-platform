from app.db.database import AsyncSessionLocal

from contextlib import asynccontextmanager

from app.db.database import (
    AsyncSessionLocal
)

async def get_db():

    async with AsyncSessionLocal() as session:
        yield session


@asynccontextmanager
async def get_new_db():

    db = AsyncSessionLocal()

    try:
        yield db

    finally:
        await db.close()