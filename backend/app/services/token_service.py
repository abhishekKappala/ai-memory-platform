import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str):

    return len(
        encoding.encode(text)
    )

def count_context_tokens(
    messages
):

    total=0

    for m in messages:

        total+=(
            count_tokens(
                m[
                    "content"
                ]
            )
        )

    return total