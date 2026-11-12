# Day 2 - Classes, Objects, and Dataclasses

## 1. Classes and Objects

A **class** is a blueprint for creating objects.

An **object** is a concrete instance of a class.

Example:

```python
class RangeRule:
    def __init__(self, minimum: float, maximum: float):
        self.minimum = minimum
        self.maximum = maximum

    def contains(self, value: float) -> bool:
        return self.minimum <= value <= self.maximum
```

Create an object:

```python
rule = RangeRule(10, 20)
```

Here, `rule` is an object of the class `RangeRule`.

---

## 2. Constructor

`__init__` initialized a new object.

```python
def __init__(self, minimum: float, maximum: float):
    self.minimum = minimum
    self.maximum = maximum
```

The values passed when creating the object are stored as attributes.

```python
rule = RangeRule(10, 20)
```

Results in:

```text
rule.minimum -> 10
rule.maximum -> 20
```

---

## 3. Attributes

Attributes store the state of an object.

Example:

```python
self.minimum
self.maximum
```

Different objects can contain different attribute values.

---

## 4. Methods and `self`

A **method** is a function that belogs to a class.

```python
def contains(self, value: float) -> bool:
    return self.minimum <= value <= self.maximum
```

`self` refers to the current object.

Therefore, the method can access the object's attributes.

Example:

```python
rule.contains(15)
```

---

## 5. When to Use a Class

A class is useful when:

- data belangs together
- behaviour belongs to that data
- a clear data type should be modeled

Example:

```text
RangeRule
├── minimum
├── maximum
└── contains()
```

A class is not necessary for every problem.

For small stateless helper operations, a normal function is often simpler.

---

## 6. Dataclasses

A `dataclass` is usefule for classes whose main purpose is storing structured data.

Example:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class ValidationIssue:
    path: str
    code: str
    message: str
```

Python automatically creates useful functionality such as:

- constructor
- readable representation
- comparisons

Instead of manually writing a large `__init__`.

---

## 7. `frozen=True`

Example:

```python
@dataclass(frozen=True)
class CatalogItem:
    id: str
    name: str
    value: float
    enabled: bool = True
```

With:

```python
frozen=True
```

the fields should not normally be changed after the object has been created.

This is useful for data that should represent a stable result.

---

## 8. Default Attribute Values

Dataclasses can contain default values:

```python
enabled: bool = True
```

Therefore:

```python
CatalogItem(
    id="item-001",
    name="Example",
    value=42,
)
```

automatically uses:

```text
enabled = True
```

---

## 9. Dictionary to Dataclass

Controlled dictionary data can be converted manually:

```python
raw = {
    "id": "item-001",
    "name": "Example",
    "value": 42,
    "enabled": True,
}
```

Convert it:

```python
item = CatalogItem(
    id=raw["id"],
    name=raw["name"],
    value=raw["value"],
    enabled=raw["enabled"],
)
```

The dictionary contains raw data.

The dataclass represents structured program data.

---

## 10. Validate Raw Data First

External JSON data must not automatically be assumed to be correct.

For example, this may be missing:

```python
raw["name"]
```

or may contain the wrong type:

```python
"value": "not a number"
```

Therefore, the general idea is:

```text
raw JSON data
    ↓
validate data
    ↓
create strict data model
```

Do not convert unverified input directly into strict dataclass objects.

---

## 11. `ValidationIssue`

A validation problem can be modeled as structured data:

```python
@dataclass(frozen=True)
class ValidationIssue:
    path: str
    code: str
    message: str
```

Example conceptually:

```text
path    → where the problem occurred
code    → type of problem
message → readable explanation
```

This is better than passing unrelated strings around separately.

---

## 12. `FileValidationResult`

A complete file result can contain the file path and all discovered issues:

```python
@dataclass(frozen=True)
class FileValidationResult:
    file_path: Path
    issues: list[ValidationIssue]

    def is_valid(self) -> bool:
        return len(self.issues) == 0
```

Here:

```text
file_path
issues
```

are data.

```text
is_valid()
```

is behavior belonging to that data.

---

## 13. Optional Return Values

A function may return an object or `None`.

Example:

```python
def first_issue(
    issues: Sequence[ValidationIssue],
) -> ValidationIssue | None:
    return issues[0] if issues else None
```

The result is:

```text
ValidationIssue → if an issue exists
None            → if no issue exists
```

---

## 14. `Sequence`

`Sequence` can describe ordered collections without requiring one specific collection type.

```python
from collections.abc import Sequence
```

Example:

```python
def first_issue(
    issues: Sequence[ValidationIssue],
) -> ValidationIssue | None:
    ...
```

The function therefore describes what kind of collection behavior it needs rather than requiring exactly a `list`.

---

## 15. Type Aliases

Complex types can be given readable names.

Example:

```python
JsonObject = dict[str, object]
```

Instead of repeatedly writing:

```python
dict[str, object]
```

you can use:

```python
JsonObject
```

This can make larger function signatures easier to understand.

---

## Key Takeaways

- A class is a blueprint; an object is an instance of that class.
- `__init__` initializes an object.
- Attributes store object state.
- Methods contain behavior related to the object.
- Use classes when data and behavior logically belong together.
- Dataclasses are useful for structured data models.
- `frozen=True` makes the model effectively immutable after creation.
- Raw JSON data should be validated before converting it into strict models.
- `X | None` means a function can return either `X` or `None`.
- Type aliases can make complex types easier to read.
- `models.py` should contain the structured data types used by the validator.