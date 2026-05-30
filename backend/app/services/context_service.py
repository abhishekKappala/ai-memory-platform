from app.models.message import Message


def build_conversation_context(
    messages: list[Message]
):

    context = []

    for message in messages:

        context.append(
            {
                "role": message.role,
                "content": message.content
            }
        )

    return context