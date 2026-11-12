from models import IssueCode, ValidationIssue


def is_non_empty_string(value: str) -> bool:
    if not isinstance(value, str):
        return False
    return value.strip() != ""

def field_exists(settings: dict[str, object], field: str):
    return field in settings

def is_non_boolean_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)

def is_list_of_non_empty_strings(value: object) -> bool:
    if not isinstance(value, list):
        return False

    for v in value:
        if not is_non_empty_string(v):
            return False

    return True


def validate_document(data: object) -> list[ValidationIssue]:
    issues = []

    if not isinstance(data, dict):
        issues.append(
            ValidationIssue(
                code = IssueCode.ROOT_IS_NOT_JSON_OBJECT,
                message = "Root is no JSON object."
            )
        )
        return issues

    if field_exists(data, "name"):
        if not is_non_empty_string(data["name"]):
            issues.append(
                ValidationIssue(
                    code = IssueCode.NAME_IS_EMPTY,
                    message = "Field 'name' is empty."
                )
            )
    else:
        issues.append(
            ValidationIssue(
                code = IssueCode.NAME_NOT_EXIST,
                message = "Field 'name' does not exist."
            )
        )

    if field_exists(data, "version"):
        if not is_non_boolean_integer(data["version"]):
            issues.append(
                ValidationIssue(
                    code = IssueCode.VERSION_NOT_NON_BOOLEAN_INTEGER,
                    message = "Field 'version' is not a non boolean integer."
                )
            )
        elif data["version"] < 1:
            issues.append(
                ValidationIssue(
                    code = IssueCode.VERSION_SMALLER_ONE,
                    message = "Field 'version' is smaller than 1."
                )
            )
    else:
        issues.append(
            ValidationIssue(
                code = IssueCode.VERSION_NOT_EXIST,
                message = "Field 'version' does not exist."
            )
        )

    if field_exists(data, "enabled"):
        if not isinstance(data["enabled"], bool):
            issues.append(
                ValidationIssue(
                    code = IssueCode.ENABLED_NOT_BOOL,
                    message = "Field 'enabled' is not bool."
                )
            )
    else:
        issues.append(
            ValidationIssue(
                code = IssueCode.ENABLED_NOT_EXIST,
                message = "Field 'enabled' does not exist."
            )
        )

    if field_exists(data, "features"):
        if not is_list_of_non_empty_strings(data["features"]):
            issues.append(
                ValidationIssue(
                    code = IssueCode.FEATURES_NOT_LIST_OF_NON_EMPTY_STRINGS,
                    message = "Field 'features' is not a list of non empty string."
                )
            )
    else:
        issues.append(
            ValidationIssue(
                code = IssueCode.FEATURES_NOT_EXIST,
                message = "Field 'features' does not exist."
            )
        )

    return issues