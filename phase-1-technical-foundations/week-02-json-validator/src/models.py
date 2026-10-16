from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ValidationIssue:
    path: str
    code: str
    message: str

@dataclass(frozen=True)
class FileValidationResult:
    file_path: Path
    issues: list[ValidationIssue]

    def is_valid(self) -> bool:
        return not self.issues