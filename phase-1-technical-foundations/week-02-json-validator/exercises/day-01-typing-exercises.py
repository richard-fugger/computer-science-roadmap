from pathlib import Path

JsonObject = dict[str, object]

def to_paths(values: list[str]) -> list[Path]:
    paths = []
    for item in values:
        paths.append(Path(item))
    return paths

def search_by_id(values: list[JsonObject], item_id: str) -> JsonObject | None:
    if item_id == "":
        return None
    for value in values:
        if value.get("id") == item_id:
            return value

    return None

