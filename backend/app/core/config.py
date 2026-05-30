from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(
    BaseSettings
):

    DATABASE_URL:str

    GROQ_API_KEY:str

    REDIS_URL:str

    SECRET_KEY:str

    ALGORITHM:str

    ACCESS_TOKEN_EXPIRE_MINUTES:int

    MAX_CONTEXT_TOKENS:int=4000

    HF_API_TOKEN:str

    HF_EMBED_MODEL:str

    STM_MESSAGE_LIMIT: int = 10

    STM_LIMIT: int = 8

    SUMMARY_LIMIT: int = 3

    MEMORY_LIMIT: int = 5

    MMR_LAMBDA: float = 0.7

    MMR_TOP_K: int = 5

    SUMMARY_TRIGGER_MESSAGE_COUNT: int = 4

    model_config=SettingsConfigDict(

        env_file=".env",

        extra="ignore"
    )


settings=Settings()



# 2..........................................................
# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):

#     APP_NAME: str = "AI Memory Platform"

#     DATABASE_URL: str

#     SECRET_KEY: str
#     ALGORITHM: str
#     ACCESS_TOKEN_EXPIRE_MINUTES: int

#     GROQ_API_KEY: str

#     MAX_CONTEXT_TOKENS: int = 4000

#     RECENT_MESSAGE_LIMIT: int = 12

#     SYSTEM_PROMPT_TOKENS: int = 500

#     MEMORY_BUDGET_TOKENS: int = 1000

#     SUMMARY_TRIGGER_MESSAGE_COUNT: int = 2

#     REDIS_URL: str

#     STM_MESSAGE_LIMIT: int = 10

#     STM_LIMIT: int =8

#     SUMMARY_LIMIT: int =3

#     MEMORY_LIMIT: int =5
    
#     class Config:
#         env_file = ".env"

# settings = Settings()

# 1.......................................................................

# from pydantic_settings import BaseSettings


# class Settings(BaseSettings):
#     APP_NAME: str = "AI Memory Platform"
#     DEBUG: bool = True

#     class Config:
#         env_file = ".env"


# settings = Settings()
