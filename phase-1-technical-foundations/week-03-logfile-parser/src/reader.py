from collections.abc import Iterator
from pathlib import Path


def iter_lines(path: Path) -> Iterator[tuple[int, str]]:
    with open(path, "r", encoding="utf-8") as file:
        for index, line in enumerate(file, start=1):
            yield index, line.rstrip("\r\n")



