from sqlalchemy.ext.asyncio import AsyncSession

from app.models.summary import Summary

from sqlalchemy.future import select


async def create_summary(
    db: AsyncSession,
    session_id: int,
    content: str
):

    summary = Summary(
        session_id=session_id,
        content=content
    )

    db.add(summary)

    await db.commit()

    await db.refresh(summary)

    return summary

async def get_session_summaries(
    db,
    session_id
):

    result = await db.execute(
        select(Summary)
        .where(Summary.session_id == session_id)
        .order_by(Summary.created_at)
    )

    return result.scalars().all()

