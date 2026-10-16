# Day 1 - Modules, Packages, Imports, and Type Annotations

## 1. Modules

A **module** is a Python file containing code such as funtions, classes, or variables.

Example:

```text
src/
├── main.py
└── loader.py
```

Both `main.py` and `loader.py` are modules.

Code from another module can be imported:

```python
from src.loader import load_json
```

---

## 2. Packages

A **package** is a directory containing related Python modules.

Example:

```text
src/
├── __init__.py
├── main.py
└── loader.py
```

Here, `src` is a package.

`__init__.py` marks the dictionary as a Python package and can also contain package initialization code.

---

## 3. Imports

Imports make code from another module available.

Example:

```python
from src.loader import load_json
```

This imports the function `load_json` from `loader.py`.

Imports help split larger programs into multiple focused modules instead of keeping everything in one file.

---

## 4. Entry Point

The **entry point** is where program execution starts.

For this project:

```text
src/main.py
```

Example:

```python
def main() -> None:
    print("JSON validator started")

if __name__ == "__main__":
    main()
```

## 5. `__name__=="__main__"`

Python automatically assigns a value to the variable `__name__`.

When a file is started directly:

```powershell
python src/main.py
```

then:

```python
__name__ == "__main__"
```

is `True`.

When the module is imported:

```python
import src/main
```

`__name__` contains the module name instead.

```text
src.main
```

Therefore, this code:

```python
if __name__ == "__main__:
    main()
```

prevents `main()` from running automatically when the module in imported.

---

## 6. Running a Module

A Python file can be started directly:

```powershell
python src/main.py
```

or as a module:

```powershell
python -m src.main
```

`-m?  tells Python to run a module using its package/module name.

---

## 7. Type Annotations

Type annotations describe which types a function expects abd returns.

Example:

```python
def normalize_paths(path: list[str]) -> list[Path]
```

Thsi means:

```text
Input: list of strings
Output: list of Path objects
```

Type annotations usually do **not enforce types at runtime**.

They mainly help:

- make expectations visible
- improve editor support
- make code easier
- support static type checking later

---

## 8. `None` in Types

A function may sometimes return no value.

Example:

```python
def find_by_id(...) -> dict[str, object] | None:
    ...
```

This means the result can be:

```text
dictionary
OR
None
```

For example, `None` can mean that no matching element was found.

In modern Python:

```python
str | None
```

expresses the same basic idea as:

```python
Optional[str]
```

---

## 9. Type Aliases

A type alias gives a complex type a readable name.

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

Example:

```python
def process(data: JsonObject) -> None:
    ...
```

Type aliases improve readability, especially when the same type appears repeatedly.

---

## 10. Minimal JSON Loader

A separate module can handle loading JSON files:

```python
import json
from pathlib import Path

def load_json(path: Path) -> object:
    with path.open("r", encoding = "utf-8") as file:
        return json.load(file)
```

For Day 1, only the normal successful case is required.

Detailed error handling comes later.

---

## 11. Program Flow

The minimal validator should work conceptually like this:

```text
CLI argument
    ↓
Path object
    ↓
load_json()
    ↓
loaded Python object
    ↓
print its type
```

`argparse` from Week 1 can be reused to receive the JSON file path.

---

## 12. Key Takeaways

- A module is a Python file.
- A package groups related modules.
- Imports make code from other modules available.
- `main.py` is the program's entry point.
- The `__main__` guard prevents `main()` from running during an import.
- Type annotations describe expected types but normally do not enforce them at runtime.
- `X | None` means a value can either be of type `X` or `None`.
- Type aliases make repeated complex types easier to read.
- `loader.py` should handle JSON loading while `main.py` coordinates the program.