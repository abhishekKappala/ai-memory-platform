from app.services.memory_chunk_service import (
    build_message_chunk, build_user_message_chunk
)

from app.services.summarization_service import (
    generate_summary
)

from app.services.summary_service import (
    create_summary
)

from app.services.chat_service import (
    get_session_messages
)

from app.core.config import settings

from app.services.memory_extraction_service import (
    extract_memories
)

from app.services.memory_service import (
    create_memory
)


async def process_memory_pipeline(
    db,
    session_id,
    user_id
):
    print("PIPELINE USER:")
    print(user_id)
    print("=" * 50)
    print("MEMORY PIPELINE STARTED")
    print("=" * 50)

    messages = await get_session_messages(
        db,
        session_id
    )

    if (
        len(messages)
        < settings.SUMMARY_TRIGGER_MESSAGE_COUNT
    ):
        print("LEN OF MESSSAGES = ", len(messages))
        print("messages")
        print(messages)
        return


    old_messages = messages[:-2]
    old_messages2 = messages[:-2]
    print("Messages")
    print(messages)
    print("OLD MESSAGES")
    print(old_messages)
    print("OLD MESSAGES")
    print(old_messages2)

    conversation_chunk = build_message_chunk(
        old_messages
    )

    user_chunk = build_user_message_chunk(
        old_messages2
    )

    print("MESSAGE COUNT:", len(messages))
    print("OLD MESSAGE COUNT:", len(old_messages))
    print("CONVERSATION CHUNK:")
    print(conversation_chunk)
    summary = await generate_summary(
        conversation_chunk
    )
    
    print("*"*50)
    print("SUMMARY GENERATED")
    print(summary)

    ## here only user queries should be used:  
    memories = await extract_memories(
        user_chunk
    )


    for memory in memories:
        await create_memory(
            db,
            user_id,
            memory
        )
    


    print("INSERTING SUMMARY")
    await create_summary(
        db,
        session_id,
        summary
    )
    print("SUMMARY INSERTED")