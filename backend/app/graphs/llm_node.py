from app.services.llm_service import (
    generate_ai_response
)


async def llm_node(
    state
):

    response=(
        await generate_ai_response(

            state[
                "context"
            ]
        )
    )

    state[
        "response"
    ]=response

    return state