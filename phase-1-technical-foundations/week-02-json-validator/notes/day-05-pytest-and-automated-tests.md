# Day 5 - Automated Tests with pytest

## 1. Why Automated Tests?

Automated tests check whether code bahaves as expected.

Compared with manual testing, they are:

- repeatable
- faster to rerun
- useful for detecting regressions
- better for checking edge cases systematically

For this project, validation logic can be tested with Python values without reading files.

---

## Installing pytest

Activate the virtual environment and install pytest:

```powershell
python -m pip install pytest
```

Check the installation

```powershell
python -m pytest --version
```

Add the dependency to:

```text
requirements.txt
```

For this week, a simple entry is sufficient:

```text
pytest
```

## 3. Arrange, Act, Assert

A test usually contains three logical parts:

```text
Arrange
→ prepare test data

Act
→ execute the code being tested

Assert
→ verify the result
```

Example:

```python
def test_valid_document_has_no_issues():
    # Arrange
    data = {
        "items": [
            {
                "id": "item-001",
                "name": "Example",
                "value": 42,
            }
        ]
    }

    # Act
    issues = validate_document(data)

    # Assert
    assert issues = []
```

The explicit comments are optional once the structure is clear.

---

## 4. Unit Tests

A **unit test** checks a small piece of logic in isolation.

Example:

```text
validate_document()
```

with a manually created Python dictionary.

Useful validator cases include:

- valid document
- missing `items`
- `items` with wrong type
- missing `id`
- empty `id`
- duplicate `id`
- `value` below `0`
- `value` above `100`
- boundary values `0` and `100`
- invalid `enabled` type

---

## 5. Testing Expected Exceptions

pytest can verify that a specific exception is raised.

```python
with pytest.raises(InvalidJsonError):
    load_json(file_path)
```

This is useful for cases such as:

- invalid JSON
- missing file

The test passes only if the expected exception occurs.

---

## 6. `tmp_path`

pytest provides `tmp_path` for temporary test files.

Example:

```python
def test_invalid_json_raises_error(tmp_path):
    file_path = tmp_path / "broken.json"

    file_path.write_text(
        "{ invalid",
        encoding="utf-8",
    )

    with pytest.raises(InvalidJsonError):
        load_json(file_path)
```

The temporary directory is created for the test and avoids depending on permanent local files.

---

## 7 Parameterized Tests

When the same rule should be tested with several inputs, pytest can run one test multiple times.

```python
@pytest.mark.parameterize(
    "value",
    [-1, 101, True, "42", None]
)
def test_invalid_values_are_rejected(value):
    ...
```

This avoids duplicating nearly identical tests.

`True` is an important test case because:

```python
isinstance(True, int)
```

returns:

```python
True
```

in Python.

---

## 8. Test Helpers

If many tests need similar valid input, a small helper can reduce duplication.

Example:

```python
make_document()
```

It can provide valid default values and allow individual fileds to be changed.

The helper should stay simple enough that the actual test case remains obvious.

---

## 9. Integration Tests

An **integration test** checks whether multiple pasts of the program work together.

Example flow:

```text
create JSON file
    ↓
load_json()
    ↓
validate_document()
    ↓
check result
```

Example:

```python
def test_file_can_be_loaded_and_validated(tmp_path):
    file_path = tmp_path / "data.json"

    file_path.write_text(
        '{"items": [{"id": "a", "name": "A", "value": 10}]}',
        encoding="utf-8",
    )

    data = load_json(file_path)
    issues = validate_document(data)

    assert issues == []
```

## 10. Unit Test vs Integration Test

### Unit Test

Cheks one small unit in isolation.

Example:

```text
validate_item()
```

with a Python dictionary.

### Integration Test

Checks multiple components working together.

```text
file
→ loader
→ validator
```

---

## 12. Running Tests

Run the complete test suite with:

```powershell
python -m pytest -q
```

`-q` means quiet mode and produces a more compact result.

---

## Key Takeaways

- Automated tests make checks repeatable.
- pytest discovers and runs test functions automatically.
- Tests should follow Arrange → Act → Assert.
- Unit tests check small pieces of logic.
- Integration tests check multiple components together.
- `pytest.raises()` tests expected exceptions.
- `tmp_path` provides temporary files and directories.
- `@pytest.mark.parameterize` runs the same test with multiple inputs.
- Test helpers can reduce duplication but should remain simple.
- Pure functions are usually easier to test than code mixed with input/output.