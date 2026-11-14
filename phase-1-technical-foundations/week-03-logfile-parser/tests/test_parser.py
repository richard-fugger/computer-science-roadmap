import pytest

from src.parser import parse_line


def make_log(
        *,
        timestamp: str,
        level: str,
        component: str,
        message: str
):
    return f"{timestamp} {level} {component} {message}"

def test_valid_error_line_returns_correct_attributes():
    # arrange
    timestamp_str = "2026-08-15 10:21:33"
    level = "ERROR"
    component = "[auth]"
    message = "Invalid token"

    error_log = make_log(timestamp = timestamp_str, level = level, component = component, message = message)

    # act
    entry = parse_line(error_log)

    # assert
    assert str(entry.timestamp) == timestamp_str and entry.level == level and entry.component == component and entry.message == message


@pytest.mark.parametrize(
        "value",
        ["NOT DEFINED", "", " ", "Error"]
)
def test_invalid_level_returns_none(value):
    timestamp_str = "2026-08-15 10:21:33"
    component = "[auth]"
    message = "Invalid token"
    
    log = make_log(timestamp = timestamp_str, level = value, component = component, message = message)

    entry = parse_line(log)

    assert entry == None

@pytest.mark.parametrize(
        "value",
        ["[AUTH]", "", " "]
)
def test_invalid_component_returns_none(value):
    timestamp_str = "2026-08-15 10:21:33"
    level = "WARNING"
    message = "Invalid token"
    
    log = make_log(timestamp = timestamp_str, level = level, component = value, message = message)

    entry = parse_line(log)

    assert entry == None

@pytest.mark.parametrize(
        "value",
        ["", " "]
)
def test_invalid_message_returns_none(value):
    timestamp_str = "2026-08-15 10:21:33"
    level = "WARNING"
    component = "[db]"
    
    log = make_log(timestamp = timestamp_str, level = level, component = component, message = value)

    entry = parse_line(log)

    assert entry == None

@pytest.mark.parametrize(
        "value",
        ["206-08-15 10:21:33", "2026-8-15 10:21:33", "2026-08-5 10:21:33", "2026-08-15 1:21:33", "2026-08-15 10:1:33", "2026-08-15 10:21:3", "08-15 10:21:33", "2026-08-15 10:21", "", " "]
)
def test_invalid_timestamp_format_returns_none(value):
    level = "WARNING"
    component = "[db]"
    message = "Invalid token"
    
    log = make_log(timestamp = value, level = level, component = component, message = message)

    entry = parse_line(log)

    assert entry == None

@pytest.mark.parametrize(
        "value",
        ["206-02-30 10:21:33", "2026-08-15 25:21:33", "2026-28-15 25:21:33", "2026-08-15 25:61:33"]
)
def test_invalid_timestamp_range_returns_none(value):
    level = "WARNING"
    component = "[db]"
    message = "Invalid token"
    
    log = make_log(timestamp = value, level = level, component = component, message = message)

    entry = parse_line(log)

    assert entry == None