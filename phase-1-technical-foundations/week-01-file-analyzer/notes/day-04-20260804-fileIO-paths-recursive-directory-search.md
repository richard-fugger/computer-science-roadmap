# File I/O, Paths, and Recursive Directory Search
**Start:** 05.08.2026 | 00:23

**Pause:** 05.08.2026 | 01:31

**Pause end:** 05.08.2026 | 10:30

**End:**

## Block 1: Repetition of Yesterday

Draw the current program flow of `main.py`:

* reads the directory from which the program was started,
* collects files from the current working directory and converts them into `list[dict]`,
* counts extensions an converts them `dict[str, int]`,
* calculates the total size of files,
* filters out the 3 largest files,
* prints a formated report of those information

---

## Block 2: Paths and File I/O in Python

Python provides the `pathlib` module for working with file and directory paths.

It also provides built-in functions such as `open()` for reading from and writing to files.

These topics are important for programs auch as file analyzer because they allow you to:

* locate files and directories,
* inspect file properties,
* search through folders,
* read file contents,
* write data to files,
* work safely with open files.

### The `Path` Class

The `Path`class represents a file system path.

Import it from `pathlib`:

```python
from pathlib import Path
```

Create a path:

```python
path = Path("example.txt")
```

This does not automatically create ao open the file.

It only creates a Python object that represents the path.

You can also represent a directory:

```python
directory = Path("documents")
```

#### Relative paths

A relative path is interpreted based on the current working directory:

```python
file_path = Path("data/example.txt")
```

#### Absolute paths

An absolute path starts from the root of the file system.

Example on Windows:

```python
file_path = Path("C:/Users/Max/Documents/example.txt")
```

Example on Linux or macOS:

```python
file_path = Path("/home/max/documents/example.txt)
```

Using `Path` is usually clearer and safer than manually combining path strings.

### Joining Paths

You can combine paths using the `/` operator:

```python
directory = Path("documents")
file_path = directory / "example.txt"
```

Result:

```powerShell
documents/example.txt
```

This works across operating systems.

Avoid manually joining paths like this:

```python
file_path = "documents/" + "example.txt"
```

Using `Path` handles the correct path separator automatically.

Example:

```python
project_directory = Path("project")
data_directory = project_directory / "data"
file_path = data_directory / "results.json"
```

### `exists()`

The `exists()` method checks whether a path exists.

```python
path = Path("example.txt")

if path.exists():
    print("The path exists.")
else:
    print("The path does not exist.")
```

It works for both files and directories.

```python
Path("example.txt").exists()
Path("documents").exists()
```

The result is a  Boolean:

```python
True
False
```

Use `exists()` when you need to check whether a file or directory is available before working with it.

### `is_file()`

The `is_file()` method checks whether a path exists and represents a regular file.

```python
path = Path("example.txt")

if path.is_file():
    print("This path is a file")
```

Example:

```python
for item in Path.cwd().iterdir():
    if item.is_file():
        print(item.name)
```

This prints only files from the current working directory.

`is_file()` returns `False` when:

* the path is a directory,
* the path does not exist,
* the path is not a regular file.

### `is_dir()`

The `is_dir()` method checks whether a path exists and represents a directory.

```python
path = Path("documents")

if path.is_dir():
    print("This path is a directory.")
```

### `iterdir()`

The `iterdir()` method returns the direct contents of a directory.

```python
directory = Path.cwd()

for item in directory.iterdir():
    print(item)
```

It inclued:

* files,
* subdirectories,
* other file system entries.

Example:

```python
for item in directory.iterdir():
    if item.is_file():
        print(f"File: {item.name}")
    if item.is_dir(): 
        print(f"Directory: {item.name}")
```

Important:

`iterdir()`is not recursive.

It only checks the immediate contents of the given directory.

Example structure:

```text
project/
├── main.py
├── README.md
└── data/
    └── results.json
```

When using:

```python
Path("project").iterdir()
```

you get:

```text
main.py
README.md
data
```

You do not directly get:

```text
data/result.json
```

### `rglob`

The `rglob` method searches recursively through a directory and all its subdirectories.

Example:

```python
directory = Path("project")

for item in directory.rglob("*"):
    print(item)
```

The `*` pattern means:

```text
Match every item
```

Example directory structure:

```text
project/
├── main.py
├── README.md
└── data/
    ├── input.json
    └── archive/
        └── old.json
```

This code:

```python
for item in Path("project").rglob("*"):
    print(item)
```

can find all entries in every nested directory.

#### Search only for specific files

Find all Python files:

```python
for file_path in directory.rglob("*.py"):
    print(file_path)
```

#### Recursive file search

If you only want files:

```python
for item in directory.rglob("*"):
    if item.is_file():
        print(item)
```

Difference:

```python
iterdir()
```

searches only the current directory.

```python
rglob("*")
```

searches the current directory and all nested directories.

### `suffix`

The `suffix`property returns the file extension.

```python
file_path = Path("main.py")

print(file_path.suffix)

# Output:
# .py
```

#### Files without an extension

```python
file_path = Path("LICENSE")

print(file_path.suffix)

# Output:
# ''
```

An empty string means that no suffix was found.

#### Files with multiple suffixes

```python
file_path = Path("archive.tar.gz")

print(file_path.suffix)

# Output:
# .gz
```

To get all suffixes:

```python
print(file_path.suffixes)

# Output
# ['.tar', '.gz']
```

### `name`

the `name` property returns the final component of a path.

```python
file_path = Path("documents/example.txt")

print(file_path.name)

# Output:
# example.txt
```

#### File name without extension

Use `stem` if you want the file name without its suffix:

```python
file_path = Path("example.txt")

print(file_path.stem)

# Output:
# example
```

Comparison:

```python
file_path.name
file_path.stem
file_path.suffix
```

Results:

```text
example.txt
example
.txt
```

### `stat()`

The `stat()` method returns information about a file or directory.

```python
file_path = Path("example.txt")

information = file_path.stat()
```

The returned object contains several properties.

For a file analyzer, the most important might be:

```pyhton
file_path.stat().st_size
```

This returns the size in bytes.

Example:

```python
size = file_path.stat().st_size

print(size)
```

Possible output:

```text
2048
```


That means the file contains 2048 bytes.

Example in a file dictionary

```python
file_info = {
    "name": file_path.name,
    "extension": file_path.suffix,
    "size": file_path.stat().st_size,
}
```

#### Other metadata

The object retured by `stat()` also contains information such as:

* modification time,
* access time,
* creation-related system information,
* file mode.

#### Important

Calling `stat()` on a path that does not exist causes an error.

You can check first:

```python
if file_path.exists():
    size = file_path.stat().st_size
```

### `resolve()`

The `resolve()` method converts a path into an absolute path.

Example:

```python
ftom pathlib import Path

directory = Path("example")
absolute_path = directory.resolve()

print(absolute_path
```

Possible output on Windows:

```text
C:\Users\Max\project\example
```

#### Why use `resulve()`

It is usefult when you want to:

* see the complete absolute path,
* remove ambiguity from relative paths,
* display the exact location of a file,
* debug path-related problems.

Example:

```python
path = Path("README.md")

print(f"Relative path: {path}")
print(f"Absolute path: {path.resolve()}")
```

### Current Working Directory

The current working directory is the directory from which the program is running.

Get it using:

```python
current_directory = Path.cwd()
```

Important:

The current working directory is not necessarily the directory in which the Python file is located.

For exmaple if you run:

```powerShell
python scripts/main.py
```

from the project root, `Path.cwd()` still returns the project root.

To get the directory containing the current Python file:

```python
script_directory = Path(__file__).parent
```

Absolute version:

```python
script_directory = Path(__file__).resolve().parent
```

### Reading Files with `open()`

Python uses the built-in `open()` function to open files.

Example:

```python
file = open("example.txt", "r", encoding="utf-8")
```

Here:

* `"example.txt"` is the file path,
* `"r"` means read mode,
* `encoding="utf-8"` defines how text is decoded.

You could read the content:

```python
content = file.read()
```

Afterwards, the file should be closed:

```python
file.close()
```

Complete example:

```python
file = open("example.txt", "r", encoding="utf-8")

content = file.read()

file.close()

print(content)
```

However, this is not the recommended form.

### Reading Files with Context Manager

The preferred way is:

```python
with open("example.txt", "r", excoding="utf-8") as file:
    content = file.read()
```

After the intented block finishes, Python automatically closes the file.

### Why use a Context Manager

The `with` statement creates a context in which a resource is used.

For files, it ensures that the file is cloes correctly.

Without a context manager:

```python
file = open("example.txt", "r", encoding="utf-8")

content = file.read()

file.close()
```

The problem is that an error may happen before `file.close()` is reached.

#### Main advantages

A context manager:

* closes the file automatically,
* works correctly when errors occur,
* reduces repeated cleanup code,
* prevents files from remaining open,
* makes the code cleaner.

### File Modes

The second argument of `open()´ defines the mode.

#### Read mode: `"r"`

```python
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Use it to read an existing file.

It causes an error if the file does not exist.

#### Write mode: `"w"`

```python
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello")
```

Use it to write to a file.

Important:

If the file already exists, its exiting content is replaced.

If it does not exist, Python creates it.

#### Append mode: `"a"`

```python
with open("example.txt", "a", encoding="utf-8") as file:
    file.write("\nNew line")
```

Use it to add content to the end of a file.

Existing content is preserved.

#### Create mode: `"x"`

```python
with open("example.txt", "x", encoding="utf-8") as file:
    file.write("New file")
```

This creates a new file.

It causes an error if the file already exists.

#### Binary modes

Binary files use modes such as:

* "rb"
* "wb"

Example:

```python
with open("image.png", "rb") as file:
    data = file.read()
```

Binary mode is used for:

* images,
* audio files,
* videos,
* compressed files,
* other non-text data.

### Why use `encoding="utf-8"`

Text files consits of bytes, but Python needs to know how those bytes represent characters.

The encoding defines that conversion.

Use:

```python
encoding="utf-8"
```

UTF-8 supports:

* English characters,
* German umlauts,
* many international writing systems,
* special characters.

Using the encoding explicitly makes the program more predictable across sytems.

Without it, Python may use platform-depentdent defaullt encoding.

### Reading an Entire File

Use `read()` to read the complete file into one string:

```python
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Example file:

```text
First line
Second line
Third line
```

The variable contains:

```text
"First line\nSecond line\nThird line"
```

This is usefule for small or medium-sized text files.

For very large files, reading everything at once may use too much memory.

### Reading One Line

Use `readline()` to read one line:

```python
with open("example.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
```

The newline character may be included:

```text
"First line\n"
```

You can remove surronding whitespace using:

```python
first_line = first_line.strip()
```

### Reading All Lines into a List

Use `readlines()`:

```python
with open("example.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
```

Possible result:

```text
[
    "First line\n",
    "Second line\n",
    "Third line\n",
]
```

Each line becomes one list element.

### Iterating Over a File

You can loop over a file directly:

```python
with open("example.txt", "r", encoding="uft-8") as file:
    for line in file:
        print(line.strip())
```

This reads the file one line at a time.

It is often better for large files because Python does not have to load the entire file into memory.

### Writing to a File

Use th `write()` method:

```python
with open("report.txt", "w", encoding="utf-8") as file:
    file.write("File Analyzer Report")
```

To write multiple lines:

```python
with open("report.txt", "w", encoding="utf-8") as file:
    file.write("File Analyzer Report\n")
    file.write("Files found: 10\n")
    file.write("Total size: 12 KB\n")
```

The newline character is:

```text
\n
```

It starts a new line.

Using `Pyth.open()`

A `Path` object also provides an `open()` method.

```python
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

you can write:

```python
file_path = Path("example.txt")
```

with file_path.open("r", encoding="utf-8") as file:
    content = file.read()

Both versions are valid.

Using `Path.open()` can be convenient when you already have a Path object.

### Convenient `pathlib` Methods

For simple operations, `Path` has shorter methods.

#### Read complete text

```python
file_path = Path("example.txt")

content = file_path.read_text(encoding="utf-8")
```

This is similar to:

```python
with file_path.open("r", encoding="utf-8") as file:
    content = file.read()
```

#### Write complete text

```python
file_path = Path("report.txt")

file_path.write_text(
    "File Analyzer Report",
    encoding="utf-8",
)
```

This is similar to opening the file in "w" mode and calling write().

These shortcuts are useful for simple cases.

A context manager is still important to understand because it is more flexible and is used for many other resources.

### Combining pathlib and File I/O

Example:

```python
from pathlib import Path


file_path = Path("example.txt")

if file_path.exists() and file_path.is_file():
    with file_path.open("r", encoding="utf-8") as file:
        content = file.read()

    print(content)
    
else:
    print("The file does not exist.")
```

This program:

* creates a path,
* checks whether it exists,
* checks whether it is a file,
* opens it safely,
* reads its content,
* closes it automatically.


