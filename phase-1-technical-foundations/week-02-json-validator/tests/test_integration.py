from src.loader import load_json
from src.validator import validate_document


def test_file_can_be_loaded_and_validated(tmp_path):
    file_path = tmp_path / "data.json"
    file_path.write_text('{"items": [{"id": "item-001", "name": "Example", "value": 50, "enabled": true}]}', encoding="utf-8")

    data = load_json(file_path)
    issues = validate_document(data)

    assert issues == []