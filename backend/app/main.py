from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.user import router as user_router
from app.api.chat import router as chat_router
from app.api.memory import router as memory_router

import time

from app.api.health import (
    router
    as
    health_router
)

from app.core.lifespan import (
    lifespan
)

from fastapi.middleware.cors import (
    CORSMiddleware
)

app=FastAPI(
    lifespan=lifespan
)


# app = FastAPI(
#     title="AI Memory Platform",
#     version="1.0.0"
# )

@app.middleware(
"http"
)

async def log_request(

    request,

    call_next
):

    start=time.time()

    response=(
        await call_next(
            request
        )
    )

    print(

        request.url,

        (
            time.time()

            -

            start

        )

        *

        1000

    )

    return response

app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        "http://localhost:3000",
        "https://ai-memory-platform-nine.vercel.app",
        "https://ai-memory-platform-jwrd.vercel.app",
        "https://ai-memory-platform-jwrd-5c1ft8dol.vercel.app",
        "https://ai-memory-platform-jwrd-89t7faxdy.vercel.app/"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(chat_router)
app.include_router(memory_router)
app.include_router(health_router)

@app.get("/")
async def root():
    return {
        "message": "AI Memory Platform Running"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }
