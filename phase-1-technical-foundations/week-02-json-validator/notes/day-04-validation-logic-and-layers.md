# Day 4 - Validation Logic and Clean Layers

## 1. Validation vs Loading

Loading and validation are different responsibilities.

```text
loader.py
→ opens files and parses JSON

validator.py
→ checks whether the loaded Python data follows the rules
```

The validator should work with normal Python values and should not open files itself.

---

## 2. Validation Schema

For this week, a valid document has this structure:

```json
{
  "items": [
    {
      "id": "item-001",
      "name": "Example item",
      "value": 42,
      "enabled": true
    }
  ]
}
```

Rules:

- root must be a JSON object
- `items` must exist
- `items` must be a list
- every item must be an object
- `id` must be a non-empty string
- every `id` must be unique
- `name` must be a non-empty string
- `value` must be a number from `0` to `100`
- `enabled` is optional
- if `enabled` exists, it must be `bool`

---

## 3. Python Number Trap

In Python:

```python
isinstance(True, int)
```

returns:

```python
True
```

because `bool` is a subclass of `int`.

Therefore, if booleans should not count as numbers, they must be excluded explicitly.

Conceptually:

```python
number
AND
not bool
```

---

## 4. Small Validation Functions

Validation should be split into small functions with clear responsibilities.

Possible structure:

```python
def validate_root(data: object) -> list[ValidationIssue]:
    ...


def validate_items(items: object) -> list[ValidationIssue]:
    ...


def validate_item(
    item: object,
    index: int,
    seen_ids: set[str],
) -> list[ValidationIssue]:
    ...


def validate_document(data: object) -> list[ValidationIssue]:
    ...
```

Each function should:

```text
receive data
→ check rules
→ return issues
```

It should not print anything.

---

## 5. Returning Issues Instead of Printing

Bad separation:

```python
def validate_item(...):
    print("Invalid value")
```

Better:

```python
def validate_item(...) -> list[ValidationIssue]:
    ...
```

The validation layer should only describe problems.

Another layer decides how they are displayed.

This makes the validator easier to test.

---

## 6. ValidationIssue

Each validation problem should contain at least:

```text
path
code
message
```

Example:

```python
ValidationIssue(
    path="items[2].value",
    code="value_out_of_range",
    message="value must be between 0 and 100",
)
```

### `path`

Shows where the error occurred.

Example:

```text
items[2].value
```

means:

```text
items
→ third item
→ value field
```

### `code`

A stable identifier for the error:

```text
value_out_of_range
missing_field
invalid_type
duplicate_id
```

### `message`

Human-readable explanation.

---

## 7. Why Stable Error Codes Matter

Tests should not depend only on exact error text.

For example:

```text
code = "duplicate_id"
```

can remain stable even if the message later changes.

This separates:

```text
machine-readable meaning
```

from:

```text
human-readable text
```

---

## 8. Helper Validation Functions

Small helpers can make validation rules easier to read.

Examples:

```python
def is_non_empty_string(value: object) -> bool:
    ...
```

```python
def is_number(value: object) -> bool:
    ...
```

```python
def validate_range(
    value,
    minimum=0,
    maximum=100,
):
    ...
```

These helpers should each answer one clear question.

---

## 9. Detecting Duplicate IDs

A `set` is useful for remembering IDs that were already seen.

Conceptually:

```text
first ID
→ store in set

next ID
→ check if already in set
```

Example idea:

```python
seen_ids = set()
```

If an ID already exists in `seen_ids`, it is a duplicate.

This is a good use case for sets because membership checks are fast and values are unique.

---

## 10. Validation Flow

The validator can conceptually work like this:

```text
validate_document(data)
        ↓
validate root
        ↓
get items
        ↓
validate items
        ↓
validate each item
        ↓
collect ValidationIssue objects
        ↓
return all issues
```

The goal is to collect problems instead of stopping after the first one.

---

## 11. Clean Project Layers

The intended structure is:

```text
src/
├── main.py
├── loader.py
├── models.py
├── validator.py
└── output.py
```

Responsibilities:

```text
loader.py
→ open files and parse JSON

models.py
→ define ValidationIssue and FileValidationResult

validator.py
→ check validation rules

output.py
→ display validation results

main.py
→ parse CLI arguments and coordinate everything
```

Each module should know only what it needs.

---

## 12. Full Data Flow

The program should follow this flow:

```text
CLI arguments
    ↓
Path
    ↓
loader.load_json()
    ↓
raw Python data
    ↓
validator.validate_document()
    ↓
list[ValidationIssue]
    ↓
FileValidationResult
    ↓
output.print_result()
```

This separation makes each part easier to understand and test.

---

## 13. Multiple CLI Files

`argparse` can accept one or more positional values with:

```python
nargs="+"
```

Conceptually:

```python
parser.add_argument("files", nargs="+")
```

Then the program can be called with:

```powershell
python -m src.main examples/valid.json
```

or:

```powershell
python -m src.main examples/valid.json examples/invalid-data.json
```

The result is a list of provided file arguments.

---

## Key Takeaways

- Loading and validation are separate responsibilities.
- Validation functions should receive Python data, not file paths.
- Validation problems should be returned as `ValidationIssue` objects.
- Error paths show where a problem occurred.
- Stable error codes are useful for tests and other outputs.
- Use a `set` to detect duplicate IDs.
- Remember that `bool` is a subclass of `int`.
- `validator.py` should contain no file access and no `print()` calls.
- `main.py` coordinates the modules.
- `nargs="+"` allows one or more files through the CLI.