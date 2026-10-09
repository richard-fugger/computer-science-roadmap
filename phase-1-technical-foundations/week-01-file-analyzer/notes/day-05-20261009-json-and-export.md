# JSON Reading, Writung, and Report Export
**Start:** 09.10.2026 | 15:25

**End:**

## Block 1: Repetition of Yesterday

Whats the dirfference between `Path.name` and `Path.suffix`?
* `Path.name` returns the name of the file with its extension
* `Path.suffix` only returns the file's extension

What does `rglob()`?
* `rglob()` returns the content of the working directory recursively

Why use `with open()`?
* it should be used because it ensures that the file will be closed

Which function calculates the total size in our program?
* `calculate_total_size`


## Block 2: JSON Basics

### Basics

JSON is a common text format for structures data.

Python and JSON types map like this:

| Python      | JSON        |
|-------------|-------------|
| `dict`      | `object`    |
| `list`      | `array`     |
| `str`       | `string`    |
| `int, float`| `number`    |
| `True, False` | `true, false` |
| `None`      | `null`      |

Example:
```json
analysis = {
    "directory": "D:/projects/cs-roadmap",
    "file_count": 120,
    "directory_count": 14,
    "total_size": 500000,
}
```

### Reading and Writung JSON

Import the module:

```python
import json
```

#### `json.dump()`

Writes Python data directly to a file:

```python
with open("result.json", "w", encoding="utf-8") as file:
    json.dump(
        analysis,
        file,
        indent=2,
        ensure_ascii=False,
    )
```

* `indent=2` makes the JSON reaable.
* `ensure_ascii=False` keeps characters such as ä, ö, + readable.

#### `json.load()`

Reads JSON from a file:

```python
with open("result.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
```

#### `json.dumps()`

Converts Python data into a JSON string:

```python
json_text = json.dumps(analysis, indent=2)
```

#### `json.loads()`

Converts a JSON string into Python data:

```python
data = json.loads(json_text)
```

Remember:

```text
demp -> Python -> file
load -> file -> Python

dumps -> Python -> string
loads -> string -> Python
```

### JSON Limitations

JSON supports ony a limitted number of data types.

Objects such as `Path` cannot be stored directly:

```python
Path("example.txt")
```

Convert them first:

```python
str(Path("example.txt").resolve())
```

The same applies tp other custom Python objects.

### Compare Loaded Data

After saving and loading JSON, you can verify that the data is unchanged:

```python
if loaded_data == analysis:
    print("Data matches.")
```

Python dictionaries and lists can be compared directly using ==.

### Stored More Complex Results

JSON can contaon nested dictionaries and lists.

Example:

```json
report = {
    "file_count": 10,
    "largest_files": [
        {
            "name": "data.csv",
            "size": 8192,
        },
        {
            "name": "README.md",
            "size": 4096,
        },
    ],
    "extensions": {
        ".py": 2,
        ".json": 3,
        ".md": 1,
    }
}
```

This allows the complete file-analysis result to be stored in one JSON file.

### Separate Calculation from Presentation

Instead of calculating values inside print() statements, first create one report containing all results.

```python
def create_report(directory, files, directory_count):
    return {
        "directory": str(directory.resolve()),
        "file_count": len(files),
        "directory_count": directory_count,
        "total_size": calculate_total_size(files),
        "largest_files": get_largest_files(files),
        "extensions": count_extensions(files),
    }
```

Then use the same report for different outputs:

```python
def print_report(report):
    ...
```

and: 

```python
def save_report_as_json(report, output_path):
    ...
```

The important idea is:

```text
File analysis
      ↓
create_report()
      ↓
   report
   ↙    ↘
Terminal   JSON file
```

The calculations happen only once. The presentation is separate.

### Save the Report as JSON

Example:

```python
def save_report_as_json(report, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            report,
            file,
            indent=2,
            ensure_ascii=False,
        )
```

### Terminal Redirection

PowerShell can redirect program output into files.

#### Standard output

```powershell
python src/main.py > output.txt
```

Instead of appearing in the terminal, normal output is written to output.txt.

#### Error output

```powershell
python src/main.py 2> errors.txt
```

Errors are written to errors.txt.

#### Both

```powershell
python src/main.py *> complete-output.txt
```

Both normal and errors are redirected.

### Pipes

A pipe passes the output of one command into another command.

Example:

```powershell
python src/main.py | Select-String ".json"
```

Flow:

```text
Python output
     ↓
Select-String
     ↓
matching lines only
```

This command shows only output lines containing .json.

#### Key Takeaways

* JSON stores structured data in a portable text format.
* json.dump() / json.load() work with files.
* json.dumps() / json.loads() work with strings.
* Use indent for readable JSON.
* Use UTF-8 and usually ensure_ascii=False.
* Convert unsupported objects such as Path into JSON.compatible values.
* Create one report containing all calculated data.
* Keep calculation, terminal output, and JSON export separate.
* Redirects send terminal output into files.
* Pipes pass output from one command to another