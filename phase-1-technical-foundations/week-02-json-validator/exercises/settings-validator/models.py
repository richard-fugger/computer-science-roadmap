from dataclasses import dataclass


class IssueCode:
    ROOT_IS_NOT_JSON_OBJECT = "root_is_not_json_object"
    NAME_NOT_EXIST = "name_not_exist"
    NAME_IS_EMPTY = "name_is_empty"
    VERSION_NOT_EXIST = "version_not_exist"
    VERSION_NOT_NON_BOOLEAN_INTEGER = "version_not_non_boolean_integer"
    VERSION_SMALLER_ONE = "version_smaller_one"
    ENABLED_NOT_BOOL = "enabled_not_bool"
    ENABLED_NOT_EXIST = "enabled_not_exist"
    FEATURES_NOT_EXIST = "features_not_exist"
    FEATURES_NOT_LIST_OF_NON_EMPTY_STRINGS = "features_not_list_of_non_empty_strings"

@dataclass(frozen=True)
class ValidationIssue:
    code: IssueCode
    message: str