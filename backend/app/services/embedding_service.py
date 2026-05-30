from huggingface_hub import (
    InferenceClient
)

from app.core.config import (
    settings
)


_client=None


def get_client():

    global _client

    if _client is None:

        _client=InferenceClient(
            token=
            settings.HF_API_TOKEN
        )

    return _client


def generate_embedding(
    text:str
):

    client=(
        get_client()
    )

    result=(
        client.feature_extraction(

            text,

            model=
            settings.HF_EMBED_MODEL
        )
    )

    return result.tolist()