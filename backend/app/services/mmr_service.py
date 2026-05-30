import numpy as np


def cosine_similarity(
    a,
    b
):

    return np.dot(
        a,
        b
    ) / (
        np.linalg.norm(a)
        *
        np.linalg.norm(b)
    )


def maximal_marginal_relevance(

    query_embedding,

    candidates,

    lambda_param=0.7,

    top_k=5
):

    selected=[]

    remaining=(
        candidates.copy()
    )

    while (
        remaining
        and
        len(selected)<top_k
    ):

        best=None

        best_score=-999

        for candidate in remaining:

            relevance=(
                cosine_similarity(
                    query_embedding,
                    candidate[
                        "embedding"
                    ]
                )
            )

            diversity=0

            if selected:

                diversity=max(

                    cosine_similarity(

                        candidate[
                            "embedding"
                        ],

                        s[
                            "embedding"
                        ]

                    )

                    for s
                    in selected
                )

            score=(

                lambda_param
                *
                relevance

                -

                (

                    1-lambda_param
                )

                *
                diversity

            )

            if (
                score
                >
                best_score
            ):

                best=candidate

                best_score=score

        selected.append(
            best
        )

        remaining.remove(
            best
        )

    return selected