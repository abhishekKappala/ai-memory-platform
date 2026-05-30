from typing import TypedDict


class ChatGraphState(
    TypedDict
):

    user_id:int

    session_id:int

    query:str

    context:list

    response:str