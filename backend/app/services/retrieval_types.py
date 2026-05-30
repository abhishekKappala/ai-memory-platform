from dataclasses import dataclass


@dataclass
class RetrievalResult:

    source: str

    messages: list

    latency_ms: float