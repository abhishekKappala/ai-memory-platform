import time

from langgraph.graph import (
    StateGraph
)

from app.graphs.graph_state import (
    ChatGraphState
)

from app.graphs.retrieval_node import (
    retrieval_node
)

from app.graphs.llm_node import (
    llm_node
)

from app.graphs.memory_node import (
    memory_node
)


def measure_node(
    node_name,
    fn
):

    async def wrapped(
        state
    ):

        start = time.time()

        result = await fn(
            state
        )

        elapsed = (
            time.time()
            - start
        ) * 1000

        print(
            f"{node_name}: "
            f"{elapsed:.2f} ms"
        )

        return result

    return wrapped


graph = StateGraph(
    ChatGraphState
)


graph.add_node(
    "retrieve",
    measure_node(
        "RETRIEVE",
        retrieval_node
    )
)

graph.add_node(
    "llm",
    measure_node(
        "LLM",
        llm_node
    )
)

graph.add_node(
    "memory",
    measure_node(
        "MEMORY",
        memory_node
    )
)


graph.set_entry_point(
    "retrieve"
)

graph.add_edge(
    "retrieve",
    "llm"
)

graph.add_edge(
    "llm",
    "memory"
)


chat_graph = graph.compile()