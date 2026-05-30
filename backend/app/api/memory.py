from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db

from app.core.dependencies import (
    get_current_user
)

from app.models.user import User

from app.services.memory_service import (
    get_user_memories
)

router = APIRouter(
    prefix="/memory",
    tags=["Memory"]
)


@router.get("/")
async def get_memories(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    memories = await get_user_memories(
        db,
        current_user.id
    )

    return memories