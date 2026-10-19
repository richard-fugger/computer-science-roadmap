# Day 3 - Exceptions and Controlled Error Handling

## 1. What Is an Exception?

An **exception** signals that a program cannot continue normally at a certain point.

Examples:

```python
FileNotFoundError
PermissionError
json.JSONDecodeError
ValueError
```

Different exception types represent deifferent kinds of problems.

---

## 2. `try` and `except`

Code taht may fail goes into `try`.

Expected errors are handles with `except`.

```python
try:
    data = load_json(path)
except FileNotFoundError:
    print("File no found")
```

Only catch exceptions you expect and know how to handle.

Avoid:

```python
except: Exception:
```

unless there is a specific reason, because it can hide programming errors.

---

## 3. `else`

`else` runs only if the `try` block completed without an exception.

```python
try:
    data = laod_json(path)
except InvalidJsonError:
    print("Invalid JSON")
else:
    print("JSON loaded successfully")
```

---

## 4. `finally`

`finally` alsways runs, whether an exception occured or not.

```python
try:
    ...
finally:
    print("Finished")
```

User it when cleanup must always happen.

Do not use it unnecessarily.

For files, a context manager is usually better:

```python
with path.open(...) as file:
    ...
```

---

## 5. `raise`

`raise` explicitly triggers an exception.

Example:

```python
if value < 0:
    raise ValueError("Value must not ne negative")
```

It can also be used to translate one exception into another.

---

## 6. Custom Exceptions

Projects can define their own exception types.

Example:

```python
class JsonValidatorError(Exception):
    pass


class JsonFileReadError(JsonValidatorError):
    pass


class InvalidJsonError(JsonValidatorError):
    pass
```

This creates a hierarchy:

```text
Exception
└── JsonValidatorError
    ├── JsonFileReadError
    └── InvalidJsonError
```

The common parent makes it possible to catch all validator-specific errors together.

---

## 7. Translate Technical Errors

The loader is the boundary between the file system and the rest of the program.

Technical errors can be converted into project-specific errors.

Example idea:

```text
FileNotFoundError
        ↓
JsonFileReadError
```

or:

```text
JSONDecodeError
        ↓
InvalidJsonError
```

This keeps technical details out of the rest of the application.

---

## 8. `raise ... from error`

Example:

```python
except FileNotFoundError as error:
    raise JsonFileReadError(
        f"File not found: {path}"
    ) from error
```

`from error` keeps the original exception as the cause.

This creates an exception chain:

```text
original technical error
        ↓ caused
project-specific error
```

This is useful for debugging while still exposing a clearer error to the rest of the application.

---

## 9. Exception Order Matters

Catch more specific exceptions before broader ones.

Example:

```python
except FileNotFoundError:
    ...

except PermissionError:
    ...

except OSError:
    ...
```

`FileNotFoundError` and `PermissionError` are more specific than `OSError`.

If a broad exception is caught first, the more specific handlers may never run.

---

## 10. JSON Parsing Errors

Invalid JSON syntax raises:

```python
json.JSONDecodeError
```

Useful information includes:

```python
error.lineno
error.colno
```

This allows messages such as:

```text
Invalid JSON at line 4, column 12
```

---

## 11. Loader Responsibility

The loader should handle errors related to:

- opening files
- reading files
- permissions
- parsing JSON

Conceptually:

```text
filesystem / JSON
        ↓
loader.py
        ↓
project-specific exceptions
        ↓
rest of program
```

The loader should not print terminal messages or use terminal colors.

---

## 12. CLI Responsibility

The CLI should decide how errors are shown to the user.

Example concept:

```python
try:
    data = load_json(path)
except JsonValidatorError as error:
    print(f"Error: {error}")
    return
```

This separates:

```text
error detection
```

from:

```text
error presentation
```

---

## 13. Technical Error vs User Message

Technical exception:

```text
FileNotFoundError
```

Project-level exception:

```text
JsonFileReadError
```

CLI message:

```text
Error: File not found: data.json
```

These are different layers of the same problem.

---

## 14. Stacktraces

A stacktrace shows how execution reached an error.

Read it from the bottom:

1. exception type
2. exception message
3. last relevant line in your own code
4. move upward through the function calls

Ask:

```text
Where was the error raised?
Which function called that function?
Where is the actual cause?
```

The place where an error becomes visible is not always the place where it originated.

---

## Key Takeaways

- Exceptions represent abnormal execution situations.
- Catch specific exceptions instead of blindly catching `Exception`.
- `try` contains risky code.
- `except` handles expected errors.
- `else` runs only when no exception occurred.
- `finally` always runs.
- `raise` creates or forwards exceptions.
- Custom exceptions make project errors clearer.
- `raise ... from error` preserves the original cause.
- The loader should translate technical errors.
- The CLI should decide how errors are displayed.
- Stacktraces should be read from the exception at the bottom upward.