from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from typing import Any


def print_sep() -> None:
    print("-----------------------")

# 1. Count the log levels in a manually created list of five LogEntry objects.

@dataclass(frozen=True)
class LogEntry:
    timestamp: datetime
    level: str
    component: str
    message: str

def count_by_log_level(entries: list[LogEntry]) -> Counter:
    levels = Counter()
    if entries is None:
        return levels
    for entry in entries:
        levels[entry.level] += 1
    return levels

def print_log_levels(levels: Counter) -> None:
    if levels is None:
        print("No levels were recorded")
        return
    for level, count in levels.items():
        print(f"{level}: {count}")

entries = [
    LogEntry(
        timestamp=datetime(2026, 8, 15, 10, 21, 33),
        level = "ERROR",
        component = "[auth]",
        message = "Invalid token"
    ),
    LogEntry(
        timestamp=datetime(2026, 8, 15, 10, 21, 35),
        level = "INFO",
        component = "[api]",
        message = "Request started"
    ),
    LogEntry(
        timestamp=datetime(2026, 8, 15, 10, 21, 39),
        level = "ERROR",
        component = "[auth]",
        message = "Invalid token"
    ),
    LogEntry(
        timestamp=datetime(2026, 8, 15, 10, 22, 10),
        level = "WARNING",
        component = "[db]",
        message = "Connection slow"
    ),
    LogEntry(
        timestamp=datetime(2026, 8, 15, 10, 22, 32),
        level = "CRITICAL",
        component = "[api]",
        message = "Request was denied"
    ),
]

levels = count_by_log_level(entries)
print_log_levels(levels)
print_sep()

# 2. Use Counter.most_common(3) to find the three most frequent strings.

def print_log_levels_most_common(levels: list[tuple[Any, int]]) -> None:
    if levels is None:
        print("No levels were recorded")
        return
    for level, count in levels:
        print(f"{level}: {count}")

print_log_levels_most_common(levels.most_common(3))
print_sep()

# 3. Determine the minimum and maximum of three datetime objects.

def get_timestamp_limits(timestamps: list[datetime]) -> tuple[datetime, datetime] | tuple[None, None]:
    if timestamps is None or len(timestamps) == 0:
        return None, None
    return min(timestamps), max(timestamps)

dates = [entry.timestamp for entry in entries]
date_min, date_max = get_timestamp_limits(dates)
if date_min is not None:
    print(f"Min date: {date_min}, Max date: {date_max}")
else:
    print("Date list empty")
print_sep()