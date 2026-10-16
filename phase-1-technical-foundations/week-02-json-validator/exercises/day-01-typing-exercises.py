# Day 1 - Practical Exercises
#
#
# 1. Write:
#    to_paths(values: list[str]) -> list[Path]
#
# 2. Write a function that searches a list of dictionaries
#    for an item by ID and returns either the dictionary or None.
#
# 3. Create a type alias such as:
#    JsonObject = dict[str, object]
#    and use it in at least one meaningful place.

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

