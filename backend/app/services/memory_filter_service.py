def filter_low_quality_memories(
    memories
):

    filtered = []

    for memory in memories:

        if (
            memory.importance_score < 0.4
        ):
            continue

        if (
            memory.confidence_score < 0.4
        ):
            continue

        filtered.append(memory)

    return filtered