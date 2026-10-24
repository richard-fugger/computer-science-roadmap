from src.constants import ValidationIssueCode
from src.models import ValidationIssue


def is_non_empty_string(value: object) -> bool:
    if not isinstance(value, str):
        return False

    return value.strip() != ""

def is_number(value: object) -> bool:
    return bool(isinstance(value, (int, float)) and not isinstance(value, bool))

def validate_range(value, minimum=0, maximum=100) -> bool:
    if not is_number(value):
        return False
    return not (value < minimum or value > maximum)

def field_exists(item: dict[str, object], field: str) -> bool:
    return field in item

def validate_root(items: object) -> list[ValidationIssue]:
    if not isinstance(items, dict):
        return [
            ValidationIssue(
                path = "root",
                code = ValidationIssueCode.ROOT_IS_NOT_JSON_ITEM,
                message = "The root of the JSON document has the wrong format."
            )
        ]
    return []

def validate_items(items: object) -> list[ValidationIssue]:
    if "items" not in items:
        return[
            ValidationIssue(
                path = "items",
                code = ValidationIssueCode.ITEMS_NOT_EXIST,
                message = "The Field \"items\" does not exist."
            )
        ]

    if not isinstance(items["items"], list):
        return [
            ValidationIssue(
                path = "items",
                code = ValidationIssueCode.ITEMS_IS_NOT_LIST,
                message = "The Field \"items\" has the wrong format."
            )
        ]

    return []

def validate_item(
        item: object,
        index: int,
        seen_ids: set[str],
) -> tuple[list[ValidationIssue], str | None]:
    issues = []

    if not isinstance(item, dict):
        return[
            ValidationIssue(
                path = f"items[{index}]",
                code = ValidationIssueCode.ITEM_IS_NOT_JSON_OBJECT,
                message = f"The item at index {index} is not a JSON object."
            )
        ], None

    id_exists = field_exists(item, "id")
    name_exists = field_exists(item, "name")
    value_exists = field_exists(item, "value")
    enabled_exists = field_exists(item, "enabled")

    if not id_exists:
        issues.append(
            ValidationIssue(
                path = f"items[{index}].id",
                code = ValidationIssueCode.ID_DOES_NOT_EXIST,
                message = f"The item's id at index {index} does not exist."
            )
        )

    if not name_exists:
        issues.append(
            ValidationIssue(
                path = f"items[{index}].name",
                code = ValidationIssueCode.NAME_DOES_NOT_EXIST,
                message = f"The item's name at index {index} does not exist."
            )
        )

    if not value_exists:
        issues.append(
            ValidationIssue(
                path = f"items[{index}].value",
                code = ValidationIssueCode.VALUE_DOES_NOT_EXIST,
                message = f"The item's value at index {index} does not exist."
            )
        )

    item_id = None

    if id_exists:
        if not is_non_empty_string(item["id"]):
            issues.append(
                ValidationIssue(
                    path = f"items[{index}].id",
                    code = ValidationIssueCode.ID_IS_NOT_NON_EMPTY_STRING,
                    message = f"The item's id at index {index} is not a non empty string."
                )
            )
        else:
            item_id = item["id"]

            if item["id"] in seen_ids:
                issues.append(
                    ValidationIssue(
                        path = f"items[{index}].id",
                        code = ValidationIssueCode.ID_ALREADY_EXISTS,
                        message = f"The item's id at index {index} already exists."
                    )
                )

    if name_exists and not is_non_empty_string(item["name"]):
        issues.append(
            ValidationIssue(
                path = f"items[{index}].name",
                code = ValidationIssueCode.NAME_IS_NOT_NON_EMPTY_STRING,
                message = f"The item's name at index {index} is not a non empty string."
            )
        )

    if value_exists and not validate_range(item["value"]):
        issues.append(
            ValidationIssue(
                path = f"items[{index}].value",
                code = ValidationIssueCode.VALUE_OUT_OF_RANGE,
                message = f"The item's value at index {index} is out of range (0 - 100)."
            )
        )

    if enabled_exists and not isinstance(item["enabled"], bool):
        issues.append(
            ValidationIssue(
                path = f"items[{index}].enabled",
                code = ValidationIssueCode.ENABLED_IS_NOT_BOOL,
                message = f"The item's enabled field at index {index} is not from type bool."
            )
        )

    return issues, item_id

def validate_document(data: object) -> list[ValidationIssue]:
    issues_root = []
    issues_items = []
    issues_item = []
    
    issues_root = validate_root(data)
    if len(issues_root) == 0:
        issues_items = validate_items(data)

        if len(issues_items) == 0:
            index = 0
            seen_ids = set()
            for item in data["items"]:
                val_issues, id = validate_item(item, index, seen_ids)
                issues_item.extend(val_issues)
                if id != None:
                    seen_ids.add(id)
                index += 1

    return issues_root + issues_items + issues_item

