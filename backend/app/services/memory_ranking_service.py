from datetime import datetime


def calculate_memory_score(
    memory,
    semantic_score: float
):

    importance_weight = (
        memory.importance_score * 0.35
    )

    confidence_weight = (
        memory.confidence_score * 0.20
    )

    decay_weight = (
        memory.decay_score * 0.15
    )

    retrieval_weight = (
        min(memory.retrieval_count, 10)
        * 0.03
    )

    final_score = (
        semantic_score * 0.50
        + importance_weight
        + confidence_weight
        + decay_weight
        + retrieval_weight
    )

    return final_score