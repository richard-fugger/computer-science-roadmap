import re
from datetime import datetime

from src.models import LogEntry

LOG_PATTERN = re.compile(r"(?P<timestamp>"
                         r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
                         r"\s(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2}))"
                         r"\s(?P<level>INFO|ERROR|WARNING|DEBUG|CRITICAL)"
                         r"\s(?P<component>\[[a-z]+\])"
                         r"\s(?P<message>\S.*)")

def parse_date(match: re.Match) -> datetime | None:
    try:
        date = datetime.strptime(match.group("timestamp"), "%Y-%m-%d %H:%M:%S")
        return date
    except ValueError:
        return None



def parse_line(line: str) -> LogEntry | None:

    match = LOG_PATTERN.fullmatch(line)

    if match is None:
        return None

    timestamp = parse_date(match)

    if timestamp is None:
        return None

    return LogEntry(
        timestamp,
        match.group("level"),
        match.group("component"),
        match.group("message")
    )