import json

from src.main import main


def test_cli_valid_file_returns_zero(tmp_path):
    file_path = tmp_path / "valid.json"

    file_path.write_text(
        json.dumps({
            "items": [
                {
                    "id": "item-001",
                    "name": "Example",
                    "value": 50,
                }
            ]
        }),
        encoding="utf-8",
    )

    exit_code = main([str(file_path)])

    assert exit_code == 0

def test_cli_invalid_document_returns_one(tmp_path):
    file_path = tmp_path / "invalid.json"

    file_path.write_text(
        """
        {
            "items": [
                {
                    "name": "Example",
                    "value": 50
                }
            ]
        }
        """,
        encoding="utf-8",
    )

    exit_code = main([str(file_path)])

    assert exit_code == 1

def test_cli_missing_file_returns_one(tmp_path):
    file_path = tmp_path / "missing.json"

    exit_code = main([str(file_path)])

    assert exit_code == 1

def test_cli_processes_multiple_files(tmp_path, capsys):
    valid_file = tmp_path / "valid.json"
    missing_file = tmp_path / "missing.json"

    valid_file.write_text(
        """
        {
            "items": [
                {
                    "id": "item-001",
                    "name": "Example",
                    "value": 50
                }
            ]
        }
        """,
        encoding="utf-8",
    )

    exit_code = main([
        str(missing_file),
        str(valid_file),
    ])

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "valid.json" in captured.out