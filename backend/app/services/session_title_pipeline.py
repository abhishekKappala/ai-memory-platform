from datetime import datetime

from sqlalchemy import select

from app.db.session import get_new_db

from app.models.chat_session import ChatSession

from app.services.session_title_service import (
    generate_title,
    update_session_title
)


async def generate_session_title_pipeline(
    session_id: int,
    first_message: str
):
    
    print("=" * 50)
    print("TITLE PIPELINE STARTED")
    print("SESSION ID:", session_id)
    print("=" * 50)

    async with get_new_db() as db:

        result = await db.execute(
            select(ChatSession)
            .where(
                ChatSession.id == session_id
            )
        )

        session = result.scalar_one_or_none()

        if not session:
            return

        if session.title != "New Chat":
            return

        title = await generate_title(
            first_message
        )

        print("GENERATED TITLE:")
        print(title)    

        if (
            title.upper()
            ==
            "GENERAL_CHAT"
        ):

            title = (
                "General Chat • "
                +
                datetime.now().strftime(
                    "%d %b")
            )

        await update_session_title(
            db,
            session_id,
            title
        )
        print("TITLE UPDATED")