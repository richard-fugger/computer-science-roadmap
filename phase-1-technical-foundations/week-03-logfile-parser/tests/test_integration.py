from datetime import datetime

from src.pipeline import iter_parsed_lines


def test_lines_can_be_read_and_parsed(tmp_path):
    file_path = tmp_path / "log.json"
    file_path.write_text("2026-08-15 10:21:31 INFO [api] Request started\n"
                         "invalid line\n"
                         "2026-08-15 10:21:34 WARNING [db] Connection slow")

    entries = []
    for nr, parsed_line in iter_parsed_lines(file_path):
        entries.append(parsed_line)

    assert len(entries) == 3

    assert entries[0].timestamp == datetime(2026, 8, 15, 10, 21, 31)
    assert entries[0].level == "INFO"
    assert entries[0].component == "[api]"
    assert entries[0].message == "Request started"

    assert entries[1] == None

    assert entries[2].timestamp == datetime(2026, 8, 15, 10, 21, 34)
    assert entries[2].level == "WARNING"
    assert entries[2].component == "[db]"
    assert entries[2].message == "Connection slow"