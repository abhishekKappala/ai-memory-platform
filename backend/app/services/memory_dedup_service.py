from difflib import SequenceMatcher

#***********************************
# i think similarity searchh is better at this duplicate_checking
#***********************************
def is_duplicate_memory(
    existing_text: str,
    new_text: str,
    threshold: float = 0.85
):

    similarity = SequenceMatcher(
        None,
        existing_text.lower(),
        new_text.lower()
    ).ratio()

    return similarity >= threshold