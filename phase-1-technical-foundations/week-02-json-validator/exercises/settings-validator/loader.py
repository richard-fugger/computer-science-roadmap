import json
from pathlib import Path


def load_json(file_path: Path) -> object:
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)