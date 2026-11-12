from enum import Enum

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

class ValidationIssueCode(Enum):
    ROOT_IS_NOT_JSON_ITEM = "root_is_no_json_item"
    ITEMS_NOT_EXIST = "items_not_exist"
    ITEMS_IS_NOT_LIST = "items_is_not_list"
    ITEM_IS_NOT_JSON_OBJECT = "item_is_not_json_object"
    ID_DOES_NOT_EXIST = "id_does_not_exist"
    NAME_DOES_NOT_EXIST = "name_does_not_exist"
    VALUE_DOES_NOT_EXIST = "value_does_not_exist"
    ID_IS_NOT_NON_EMPTY_STRING = "id_is_not_non_empty_string"
    ID_ALREADY_EXISTS = "id_already_exists"
    NAME_IS_NOT_NON_EMPTY_STRING = "name_is_not_non_empty_string"
    VALUE_OUT_OF_RANGE = "value_out_of_range"
    ENABLED_IS_NOT_BOOL = "enabled_is_not_bool"