from fastapi import (
    APIRouter,
    Depends,
    BackgroundTasks
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.db.session import (
    get_db
)

from app.core.dependencies import (
    get_current_user
)

from app.models.user import (
    User
)

from app.schemas.chat_schema import (
    ChatSessionCreate,
    ChatSessionResponse,
    MessageCreate
)

from app.services.chat_service import (
    create_chat_session,
    create_message,
    create_assistant_message,
    get_session_messages,
    get_user_sessions
)

from app.services.stm_service import (
    add_recent_message
)

from app.services.background_memory_service import (
    process_memory_pipeline
)

from app.graphs.chat_graph import (
    chat_graph
)

from app.services.session_title_pipeline import (
    generate_session_title_pipeline
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "/sessions",
    response_model=ChatSessionResponse
)
async def create_session(
    session_data: ChatSessionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    session = await create_chat_session(
        db,
        session_data.title,
        current_user.id
    )

    return session


@router.get(
    "/sessions",
    response_model=list[ChatSessionResponse]
)
async def get_sessions(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    return await get_user_sessions(
        db,
        current_user.id
    )


@router.post(
    "/sessions/{session_id}/messages"
)
async def send_message(
    session_id: int,
    message_data: MessageCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    user_message = await create_message(
        db,
        session_id,
        "user",
        message_data.content
    )

    add_recent_message(
        session_id,
        "user",
        message_data.content
    )

    messages = await get_session_messages(
        db,
        session_id
    )

    is_first_message = (
        len(messages) == 1
    )

    result = await chat_graph.ainvoke(

        {
            "user_id":
                current_user.id,

            "session_id":
                session_id,

            "query":
                message_data.content,

            "context":
                [],

            "response":
                ""
        }

    )

    ai_response = (
        result["response"]
    )

    assistant_message = (
        await create_assistant_message(
            db,
            session_id,
            ai_response
        )
    )

    add_recent_message(
        session_id,
        "assistant",
        assistant_message.content
    )

    background_tasks.add_task(
        process_memory_pipeline,
        db,
        session_id,
        current_user.id
    )

    if is_first_message:

        background_tasks.add_task(
            generate_session_title_pipeline,
            session_id,
            message_data.content
        )

    return {
        "user_message":
            user_message.content,

        "assistant_response":
            assistant_message.content
    }


@router.get(
    "/sessions/{session_id}/messages"
)
async def get_messages(
    session_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    return await get_session_messages(
        db,
        session_id
    )