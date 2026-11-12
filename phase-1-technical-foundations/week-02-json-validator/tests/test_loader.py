import pytest
from src.exceptions import InvalidJsonError, JsonFileReadError
from src.loader import load_json


def test_invalid_json_raises_error(tmp_path):
    file_path = tmp_path / "broken.json"
    file_path.write_text("{ invalid", encoding="utf-8")

    with pytest.raises(InvalidJsonError):
        load_json(file_path)

def test_file_not_exist_raises_error(tmp_path):
    file_path = tmp_path / "missing-json"

    with pytest.raises(JsonFileReadError):
        load_json(file_path)