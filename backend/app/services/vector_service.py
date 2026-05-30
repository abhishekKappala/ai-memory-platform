import chromadb

from app.services.embedding_service import (
    generate_embedding
)

client = chromadb.PersistentClient(
    path="chroma_db"
)


def get_collection():

    return client.get_or_create_collection(
        name="user_memories"
    )


def store_memory_embedding(
    memory_id: int,
    user_id: int,
    content: str
):


    try:

        embedding = generate_embedding(
            content
        )

        if not embedding:
            return

        get_collection().upsert(

            ids=[str(memory_id)],

            embeddings=[embedding],

            documents=[content],

            metadatas=[
                {
                    "user_id": str(user_id)
                }
            ]
        )

        print("VECTOR STORE SUCCESS")
        print(f"MEMORY ID: {memory_id}")
        print(f"USER ID: {user_id}")

    except Exception as e:

        print("VECTOR STORAGE ERROR")
        print(e)


def search_memories(
    user_id: int,
    query: str,
    top_k: int = 5
):

    try:

        query_embedding = generate_embedding(
            query
        )

        if not query_embedding:
            return {}

        results = get_collection().query(

            query_embeddings=[
                query_embedding
            ],

            n_results=top_k,

            where={
                "user_id": str(user_id)
            },

            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

        print("SEARCH QUERY:")
        print(query)

        print("VECTOR RESULTS:")
        print(results)

        return results

    except Exception as e:

        print("VECTOR SEARCH ERROR")
        print(e)

        return {}


def search_candidate_memories(
    user_id: int,
    query: str,
    top_k: int = 15
):

    try:

        query_embedding = generate_embedding(
            query
        )

        if not query_embedding:
            return {}

        results = get_collection().query(

            query_embeddings=[
                query_embedding
            ],

            n_results=top_k,

            where={
                "user_id": str(user_id)
            },

            include=[
                "documents",
                "embeddings",
                "metadatas",
                "distances"
            ]
        )

        print("SEARCH QUERY:")
        print(query)

        print("CANDIDATE RESULTS:")
        print(results)

        return results

    except Exception as e:

        print("CANDIDATE SEARCH ERROR")
        print(e)

        return {}


