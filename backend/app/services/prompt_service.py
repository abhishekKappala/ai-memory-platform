from pathlib import Path


def load_system_prompt():

    prompt_path = Path(
        "app/shared/prompts/system_prompt.txt"
    )

    return prompt_path.read_text(
        encoding="utf-8"
    )