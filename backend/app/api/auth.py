from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# 
from fastapi.security import OAuth2PasswordRequestForm

from app.db.session import get_db

from app.schemas.user_schema import (
    UserCreate,
    UserLogin,
    UserResponse
)

from app.services.auth_service import (
    create_user,
    authenticate_user
)

from app.core.token import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/signup",
    response_model=UserResponse
)
async def signup(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
):

    user = await create_user(
        db,
        user_data
    )

    return user

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):

    user = await authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# @router.post("/login")
# async def login(
#     user_data: UserLogin,
#     db: AsyncSession = Depends(get_db)
# ):

#     user = await authenticate_user(
#         db,
#         user_data.email,
#         user_data.password
#     )

#     if not user:
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid credentials"
#         )

#     token = create_access_token(
#         {
#             "sub": str(user.id)
#         }
#     )

#     return {
#         "access_token": token,
#         "token_type": "bearer"
#     }