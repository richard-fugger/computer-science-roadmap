import pytest
from src.constants import ValidationIssueCode
from src.validator import validate_document


def make_document(
    *,
    item_id = "item-001",
    name = "Example",
    value = 50,
    enabled = True
):
    return {
        "items": [
            {
                "id": item_id,
                "name": name,
                "value": value,
                "enabled": enabled,
            }
        ]
    }

def test_valid_document_returns_no_issues():
    # Arrange
    data = make_document()

    # Act
    issues = validate_document(data)

    # Assert
    assert issues == []

def test_root_of_type_list_returns_issue():
    # Arrange
    data = []

    # Act
    issues = validate_document(data)
    codes = [issue.code for issue in issues]

    # Assert
    assert ValidationIssueCode.ROOT_IS_NOT_JSON_ITEM in codes

def test_missing_items_returns_issue():
    # Arrange
    data = {
        "id": "item-001",
        "name": "Example",
        "value": 50,
    }

    # Act
    issues = validate_document(data)
    codes = [issue.code for issue in issues]

    # Assert
    assert ValidationIssueCode.ITEMS_NOT_EXIST in codes

def test_items_of_wrong_type_returns_issue():
    data = {
        "items": "item-001"
        }

    issues = validate_document(data)
    codes = [issue.code for issue in issues]

    assert ValidationIssueCode.ITEMS_IS_NOT_LIST in codes

def test_missing_id_returns_issue():
    data = {
        "items": [
            {
                "name": "Example",
                "value": 50,
            }
        ]
    }

    issues = validate_document(data)
    codes = [issue.code for issue in issues]
    
    assert ValidationIssueCode.ID_DOES_NOT_EXIST in codes

def test_missing_name_returns_issue():
    data = {
        "items": [
            {
                "id": "item-001",
                "value": 50,
            }
        ]
    }

    issues = validate_document(data)
    codes = [issue.code for issue in issues]
    
    assert ValidationIssueCode.NAME_DOES_NOT_EXIST in codes

def test_missing_value_returns_issue():
    data = {
        "items": [
            {
                "id": "item-001",
                "name": "Example",
            }
        ]
    }

    issues = validate_document(data)
    codes = [issue.code for issue in issues]
    
    assert ValidationIssueCode.VALUE_DOES_NOT_EXIST in codes

def test_empty_id_returns_issue():
    data = make_document(item_id="")

    issues = validate_document(data)
    codes = [issue.code for issue in issues]
        
    assert ValidationIssueCode.ID_IS_NOT_NON_EMPTY_STRING in codes

def test_empty_name_returns_issue():
    data = make_document(name="")

    issues = validate_document(data)
    codes = [issue.code for issue in issues]
        
    assert ValidationIssueCode.NAME_IS_NOT_NON_EMPTY_STRING in codes

def test_duplicate_id_returns_issue():
    data = {
        "items": [
            {
                "id": "item-001",
                "name": "Example-001",
                "value": 50,
            },
            {
                "id": "item-001",
                "name": "Example-002",
                "value": 51,
            }
        ]
    }

    issues = validate_document(data)
    codes = [issue.code for issue in issues]
            
    assert ValidationIssueCode.ID_ALREADY_EXISTS in codes

@pytest.mark.parametrize(
    "value",
    [0, 100]
)
def test_boundary_values_are_valid(value):
    data = make_document(value=value)
    
    issues = validate_document(data)
            
    assert issues == []

@pytest.mark.parametrize(
    "value",
    ["True", 10, -1, 1.2, None]
)
def test_enabled_of_wrong_type_returns_issue(value):
    data = make_document(enabled=value)
    
    issues = validate_document(data)
    codes = [issue.code for issue in issues]
            
    assert ValidationIssueCode.ENABLED_IS_NOT_BOOL in codes

@pytest.mark.parametrize(
    "value",
    [True, -1, 101, 100.1, -0.1, "42", None]
)
def test_invalid_value_returns_issue(value):
    data = make_document(value=value)
    
    issues = validate_document(data)
    codes = [issue.code for issue in issues]
            
    assert ValidationIssueCode.VALUE_OUT_OF_RANGE in codes