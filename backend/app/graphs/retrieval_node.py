from app.services.context_orchestrator import (
    build_context
)


async def retrieval_node(
    state
):

    state[
        "context"
    ]=(
        await build_context(

            None,

            state[
                "session_id"
            ],

            state[
                "user_id"
            ],

            state[
                "query"
            ]
        )
    )

    return state