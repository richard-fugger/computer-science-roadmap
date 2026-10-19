import json
from pathlib import Path

from src.exceptions import InvalidJsonError, JsonFileReadError


def load_json(path: Path) -> object:
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as error:
        raise JsonFileReadError(f"File not found: {path}") from error
    except PermissionError as error:
        raise JsonFileReadError(f"Permission denied: {path}") from error
    except json.JSONDecodeError as error:
        raise InvalidJsonError(f"Invalid JSON inf {path}: Row: {error.lineno}, Column: {error.colno}") from error
    except OSError as error:
        raise JsonFileReadError(f"File could not be read: {path}") from error