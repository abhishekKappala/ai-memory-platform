# from datetime import datetime
from datetime import datetime, timezone

def apply_memory_decay(memory):

    # days_old = (
    #     datetime.utcnow()
    #     - memory.created_at
    # ).days


    days_old = (
        datetime.now(timezone.utc)
        - memory.created_at
    ).days

    decay = max(
        0.3,
        1.0 - (days_old * 0.01)
    )

    return decay