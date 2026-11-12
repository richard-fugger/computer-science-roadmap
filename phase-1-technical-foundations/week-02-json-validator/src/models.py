from dataclasses import dataclass
from pathlib import Path

from src.constants import ValidationIssueCode


@dataclass(frozen=True)
class ValidationIssue:
    path: str
    code: ValidationIssueCode
    message: str

@dataclass(frozen=True)
class FileValidationResult:
    file_path: Path
    issues: list[ValidationIssue]

    def is_valid(self) -> bool:
        return not self.issues