def build_message_chunk(
    messages
):

    chunk = []

    for message in messages:

        chunk.append(
            f"{message.role}: {message.content}"
        )

    return "\n".join(chunk)


def build_user_message_chunk(
    messages
):

    chunk = []

    for message in messages:
        if message.role == "user":
            chunk.append(
                f"{message.role}: {message.content}"
            )

    return "\n".join(chunk)