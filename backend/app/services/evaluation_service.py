def evaluate_response(

    query,

    response
):

    score=0.5

    if len(
        response
    )>100:

        score+=0.1

    return min(
        score,
        1
    )