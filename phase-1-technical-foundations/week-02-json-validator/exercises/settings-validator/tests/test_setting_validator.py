import pytest
from models import IssueCode
from validator import validate_document


def make_document(
        *,
        name = "demo-app",
        version = 1,
        enabled = True,
        features = None
) -> dict[str, object]:
    if features is None:
        features = ["settings", "export"]
    return {
        "name": name,
        "version": version,
        "enabled": enabled,
        "features": features
    }

def test_name_is_empty_returns_issue():
    # Arrange
    data = make_document(name = "")

    # Act
    issues = validate_document(data)
    codes = [issue.code for issue in issues]

    # Assert
    assert IssueCode.NAME_IS_EMPTY in codes

@pytest.mark.parametrize(
    "value",
    [True, False, 0.99, 1.01, 5.8, "48"]
)
def test_version_is_not_non_boolean_integer_returns_issue(value):
    data = make_document(version=value)

    issues = validate_document(data)
    codes = [issue.code for issue in issues]

    assert IssueCode.VERSION_NOT_NON_BOOLEAN_INTEGER in codes

@pytest.mark.parametrize(
    "value",
    [0, -1]
)
def test_version_is_smaller_one_returns_issue(value):
    data = make_document(version=value)

    issues = validate_document(data)
    codes = [issue.code for issue in issues]

    assert IssueCode.VERSION_SMALLER_ONE in codes

@pytest.mark.parametrize(
    "value",
    [{}, ["settings", ""], ["settings", " "], ["", "settings"]]
)
def test_features_is_not_list_of_non_empty_strings_returns_issue(value):
    data = make_document(features=value)

    issues = validate_document(data)
    codes = [issue.code for issue in issues]

    assert IssueCode.FEATURES_NOT_LIST_OF_NON_EMPTY_STRINGS in codes