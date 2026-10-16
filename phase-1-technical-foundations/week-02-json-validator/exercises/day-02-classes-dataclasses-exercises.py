# Day 2 - Practical Exercises
#
# 1. Create a class for a small file analysis with:
#    - path
#    - number of found issues
#    - an is_valid() method
#
# 2. Build the same structure as a dataclass and compare the code.
#
# 3. Convert three controlled dictionaries into CatalogItem objects.
#
# 4. Write a function that returns ValidationIssue | None.
#
# 5. Use at least one custom type alias to make a complex signature
#    easier to read.

from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path


class ValidationIssue:
    def __init__(self, row: int, message: str):
        self.row = row
        self.message = message


class FileAnalysisC:
    def __init__(self, path: Path, issue_count: int):
        self.path = path
        self.issue_count = issue_count

    def is_valid(self) -> bool:
        return self.issue_count == 0

@dataclass(frozen=True)
class FileAnalysisDC:
    path: Path
    issue_count: int

    def is_valid(self) -> bool:
        return self.issue_count == 0

class CatalogItem:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

JsonObjects = list[dict[str, object]]

def list_dict_to_list_catalog_item(dict_list: JsonObjects) -> list[CatalogItem]:
    cat_list = []
    for item in dict_list:
        cat_list.append(
            CatalogItem(
                name = item["name"],
                age = item["age"],
            )
        )
    return cat_list


items = [
    {
        "name": "John",
        "age": 34,
    },
    {
        "name": "Max",
        "age": 17
    },
    {
        "name": "Peter",
        "age": 53,
    }
]

cat_list = list_dict_to_list_catalog_item(items)

def first_validation_issue(validations_issues: Sequence[ValidationIssue]) -> ValidationIssue | None:
    if validations_issues:
        return validations_issues[0]
    return None
