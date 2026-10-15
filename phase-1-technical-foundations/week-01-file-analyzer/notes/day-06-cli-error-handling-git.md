# Command Line, Error Handling, and Basic Git
**Start:** 10.10.2026 | 18:11

**End:** 

## 1. Command-Line Interfaces

A command-line interface (CLI) allows a program to receive input directly from the terminal.

Instead of defining a path inside the source code:

``` python
directory = Path("D:/projects/example")
```

the user can provide it when aterting the program.

```powershell
python src/main.py D:\projects\example
```

This makes the program reusable without changing the source code.

---

## 2. `argparse`

Pyhton provides the built-in `argparse` module for command-line arguments.

Basic structure:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(...)
args = parser.parse_args()
```

`ArgumentParser` defines which arguments the program accepts.

`parse_args()` reads the arguments passed through the terminal.

---

## 3. Positional Arguments

A positional argument is required and is identified by its position.

Example

```python
parser.add_argument("directory")
```

Terminal:

```powershell
python src/main.py D:\projects\example
```

Access:

```python
args.directory
```

For the file analyzer, the directory path is a positional argument.

---

## Optional Arguments

Optional arguments usually start with `--`.

Example:

```python
parser.add_argument("--output")
```

Terminal:

```powershell
python src/main.py D:\projects\example --output result.json
```

Access:

```python
args.output
```

If the argument is not provided, its value is normally `None`

---

## 5. Boolean Flags

A flag represents an on/off option.

Example:

```python
parser.add_argument("--json", action="store_true")
```

Without the flag:

```powershell
python src/main.py D:\projects\example
```

```python
args.json == False
```

With the flag:

```powershell
python src/main.py D:\projects\example --json
```

```python
args.json == True
```

---

## 6. Argument Types

`argparse` can convert values automatically.

Example:

```python
parser.add_argument("--top", type=int)
```

Terminal:

```powershell
python src/main.py D:\projects\example --top 10
```

`args.top` is then an integer.

If something like this is entered:

```powershell
--top abc
```

`argparse` reports an invalid integer automatically.

Logical restrictions such as `--top 0` or negative values may still need to be checked manually.

---

## 7. Path Validation

A path can exist without being a directory.

Useful checks with `pathlib`:

```python
path.exists()
path.is_file()
path.is_dir()
```

These cases should be distinguished:

- path does not exist
- path exists but points to a file
- path exists and is a directory

Error messages should explain the problem clearly instead of only displaying a Python exception.

---

## 8. Empty Directories

An empty directory is normally not an error.

A valid analysis can contain:

```text
Files: 0
Directories: 0
Total size: 0
```

The program should therefore handle an empty list of files correctly.

---

## 9. `try` and `except`

Operations involving files can fail even when the path exists.

Basic structure:

```python
try:
    # operation that may fail
except SomeError:
    # controlled error handling
```

Relevant errors can include:

```python
PermissionError
FileNotFoundError
OSError
```

Examples of operations that can fail:

- reading file information
- opening a file
- writing the JSON output

---

## 10. Writing Output Files

Writing can fail because, for example:

- the destination is not writable
- permissions are missing
- the path is invalid

The write operation should therefore be handled so that the user receives a readable error message instead of an unhandled traceback.

---

## 11. Program Flow

The CLI should provide input to the existing analyzer.

Conceptually:

```text
CLI arguments
    ↓
validate input
    ↓
analyze directory
    ↓
create report
    ↓
print report
    ↓
optionally export JSON
```

The analysis logic itself should not depend on where the directory path came from.

---

## 12. Git Basics

Show the commit history:

```powershell
git log --oneline
```

Show unstaged changes:

```powershell
git diff
```

Create and switch to a branch:

```powershell
git switch -c feature/cli
```

Stage and commit changes:

```powershell
git add .
git commit -m "Add command line interface"
```

Switch back:

```powershell
git switch phase-01-week-01
```

Merge the feature branch:

```powershell
git merge feature/cli
```

Basic workflow:

```text
create branch
    ↓
make changes
    ↓
commit changes
    ↓
switch back
    ↓
merge branch
```

---

## 13. README Content

The project README should explain:

- purpose of the program
- requirements
- installation
- virtual environment activation
- how to start the program
- example CLI commands
- description of the output

A README should allow another person to understand how to run the project without reading the source code first.

---

## Key Takeaways

- CLI arguments remove hardcoded user input from the source code.
- `argparse` parses positional and optional arguments.
- `action="store_true"` is useful for boolean flags.
- `type=int` converts command-line input to integers.
- Validate paths before analyzing them.
- Empty directories are valid input.
- Use `try` / `except` for operations that can fail.
- Error messages should be understandable to the user.
- Feature branches allow changes to be developed separately before merging.