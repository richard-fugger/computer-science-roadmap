from collections.abc import Iterator
from pathlib import Path

from src.models import LogEntry
from src.parser import parse_line
from src.reader import iter_lines


def iter_parsed_lines(path: Path) -> Iterator[tuple[int, LogEntry | None]]:
    for line_number, line in iter_lines(path):
        yield line_number, parse_line(line)