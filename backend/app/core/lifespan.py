from contextlib import (
    asynccontextmanager
)


@asynccontextmanager

async def lifespan(
    app
):

    print(
        "STARTING"
    )

    yield

    print(
        "STOPPING"
    )