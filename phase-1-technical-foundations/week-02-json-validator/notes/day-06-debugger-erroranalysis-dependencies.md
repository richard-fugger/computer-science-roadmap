# Day 6 - Debugger, Error Analysis, and Dependencies

## 1. Debugging Instead of Guessing

When a test fails, do not immediately change the code.

First make the problem reproducible:

```text
Given:
→ specific input

Expected:
→ expected result

Actual:
→ observed result
```

Then use the failing test as the fixed reproduction case.

---

## 2. Breakpoints

A breakpoint pauses program execution at a specific line.

This lets you inspect:

- current variable values
- variable types
- current function
- call stack
- program stat before an after a line

---

## 3. Debugger Navigation

### Step Over

Executes the current line without entering called functions.

```text
current line
→ execute
→ next line
```

VS Code shortcut:

```text
F10
```

### Step Into

Enters a function that is called on the current line.

Useful when you want to inspect what happens inside that function.

VS Code shortcut:

```text
F11
```

### Step Out

Finishes the current function and returns to the caller.

VS Code shortcut:

```text
Shift + F11
```

### Continue

Continues execution until:

- the next breakpoint
- an exception
- program end

VS Code shortcut:

```text
F5
```

### Stop Debugging

Stops the current debugging session.

VS Code shortcut:

```text
Shift + F5
```

### Debugger Controls in VS Code

The most important debugger controls are:

```text
Continue        → F5
Step Over       → F10
Step Into       → F11
Step Out        → Shift + F11
Restart         → Ctrl + Shift + F5
Stop            → Shift + F5
```

The yellow highlighted line shows the next line that will be executed.

Current local variables can be inspected under:

```text
Run and Debug
→ Variables
→ Locals
```

The current chain of active function calls can be inspected under:

```text
Run and Debug
→ Call Stack
```

---

## 4. Call Stack

The call stack shows how execution reached the current function.

Example:

```text
test_duplicate_id_returns_issue()
    ↓
validate_document()
    ↓
validate_item()
```

It helps answer:

```text
Who called thsi function?
Where did the data come from?
Where was the wrong state first created?
```

The place where an error becomes visible is not always where it originated.

---

## 5. Debugging a Failing Test

A useful workflow is:

```text
failing test
    ↓
understand expected vs actual result
    ↓
set breakpoint
    ↓
run only that test
    ↓
inspect variables
    ↓
follow call stack
    ↓
identify cause
    ↓
fix code
    ↓
rerun test
```

Do not add random `print()` statements before understanding what you want to inspect.

---

## 6. Types of Test Failures

### Failed Assertion

Example:

```python
assert issues = []
```

fails bacause the actual result differs from the expected result.

This usually means:

```text
code behaviour != test expectation
```

### Unexpected Exception

The program crashes before reaching the expected assertion.

Examples:

```text
TypeError
KeyError
AsstributeError
```

This often means the tested code does not handle the input correctly.

### Error in the Test

Sometimes the production code is correct and the test itself is wrong.

Possible causes:

- incorrect test data
- wrong expected value
- invalid JSON fixture
- wrong error code expected

Test must also be debugged critically.

---

## 7. Running Specific Tests

Run one test file:

```powershell
python -m pytest tests/test_validator.py -q
```

Run tests matching a keyword:

```powershell
python -m pytest -k duplicate -vv
``

Run one specific test:

```powershell
python -m pytest tests/test_loader.py::test_invalid_json_raises_error -vv
```

Useful options:

Useful options:

```text
-q
→ compact output

-vv
→ detailed output

-k
→ filter tests by name
```

Running only the relevant test makes debugging faster an more reproducible.

---

## 8. Deliberately Introducing a Bug

A useful debugging exercise is to temporarily introduce a known error.

Examples:

```text
add an ID to seen_ids too early
reject value 100
treat enabled=False as missing
```

Then:

```text
run relevant test
→ observe failure
→ debug
→ identify cause
→ restore correct behavior
```

The goal is to practice the debugging process, not just fixing the bug.

---

## 9. Stacktrace vs Call Stack

A **stacktrace** is usualle shown after an unhandled exception.

It tells you:

- exception type
- error message
- sequence of function calls
- source lines involved

A **call stack** in the debugger shows the active function calls while program is paused.

Both help trace execution backwards toward the cause.

---

## 10. pip

`pip` installs and manages Python packages.

Installe a package:

```powershell
python -m pip install pytest
```

Show information about a package:

```powershell
python -m pip show pytest
```

List installed packages;

```powershell
python -m pip list
```

Using:

```powershell
python -m pip
```

ensures that pip belongs to the Python interpreter you are currently using.

---

## 11. `requirements.txt`

`requirements.txt` is a simple way to document installable project dependencies.

Example:

```text
pytest
```

Install all listed dependencies with:

```pwoershell
python -m pip install -r requirements.txt
```

It helps another developer recreate the required environment.

--

## 12. `pyproject.toml`

`pyproject.toml` is a central configuration file ussed by many modern Python projects.

It can contain:

- project metadata
- Python requirements
- dependencies
- build-system configuration
- settings for tools such as formatters, linters, or test tools

---

## 13. Making the CLI More Testable

A CLI can accept arguments as a parameter instaed of of depending onyl on `sys.argv`.

Example pattern:

```python
def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    ...

    return 0
```

Program entry:

```python
if __name__ == "__main__":
    raise SystemExit(main())
```

This allows tests to call:

```python
main(["example/valid.json"])
```

instead of starting a separate terminal process.

---

## 14. Exit Codes

A CLI can return an interger status code.

Typical idea:

```text
0
→ success

non-zero
→ some kind of failure
```

`SystemExit(main())` passes the returned code to the operating system.

This can make command-line programs easier to automate and test.

---

## 15. README

The README should now explain at least:

```text
project purpose
Python version
virtual environment
pytest installation
valid JSON example
CLI usage
multiple-file usage
how to run tests
project structure
```

A new developer should be able to underatand how to run and test the project withou reading all source files first.

---

## Key Takeaways

- Reproduce a bug before changing code.
- Use a failing test as a stable debugging case.
- Breakpoints let you inspect program state.
- Step Over, Step Into, Step Out, and Continue control debugger execution.
- The call stack shows how execution reached the current function.
- Debug the cause, not only the visible symptom.
- Run individual tests to make debugging faster.
- `rewuirements.txt` documents simple project dependencies.
- `pyproject.toml` is a central configuration file in modern Python projects.
- A CLI becomes easier to test when arguments can be passed directly to `main()` or `parse_args()`.