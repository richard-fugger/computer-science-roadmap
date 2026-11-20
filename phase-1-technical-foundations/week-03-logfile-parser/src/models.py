from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(frozen=True)
class LogEntry:
    timestamp: datetime
    level: str
    component: str
    message: str

@dataclass(frozen=False)
class LogReport:
    path: Path
    total_lines: int
    valid_lines: int
    by_level: Counter
    by_component: Counter
    error_messages: Counter
    first_error: datetime
    last_error: datetime

    def update_report(self, log: LogEntry | None) -> None:
        self.total_lines += 1
        if log is None:
            return
        self.valid_lines += 1
        self.by_level[log.level] += 1
        self.by_component[log.component] += 1 
        if log.level == "ERROR" or log.level == "CRITICAL":
            self.error_messages[log.message] += 1
            self.first_error = min(self.first_error, log.timestamp)
            self.last_error = max(self.last_error, log.timestamp)
