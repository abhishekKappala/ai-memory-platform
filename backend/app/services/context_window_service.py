from app.services.token_service import (
    count_tokens
)

from app.services.prompt_service import (
    load_system_prompt
)

from app.core.config import settings

from app.services.stm_service import (
    get_recent_messages
)


def build_recent_message_window(
    messages,
    summaries
):

    context = []

    system_prompt = {
        "role": "system",
        "content": load_system_prompt()
    }

    context.append(system_prompt)

    # ADD SUMMARIES
    for summary in summaries:

        context.append(
            {
                "role": "system",
                "content": f"Conversation Summary: {summary.content}"
            }
        )

    # KEEP RECENT RAW MESSAGES
    recent_messages = messages[
        -settings.RECENT_MESSAGE_LIMIT:
    ]

    total_tokens = 0

    selected_messages = []

    for message in reversed(recent_messages):

        token_count = count_tokens(
            message.content
        )

        if (
            total_tokens + token_count
            > settings.MAX_CONTEXT_TOKENS
        ):
            break

        selected_messages.insert(
            0,
            {
                "role": message.role,
                "content": message.content
            }
        )

        total_tokens += token_count

    context.extend(selected_messages)

    return context


def build_hot_context(
    session_id,
    summaries
):

    recent = get_recent_messages(
        session_id
    )

    system = {
        "role":"system",
        "content":
        load_system_prompt()
    }

    return [
        system,
        *summaries,
        *recent
    ]