# Functions, Parameters, and Clean Structure
**Start:** 04.08.2026 | 00:25

---

## Block 1: Repetition of Yesterday

Write a function that should return a dictionary containing the count of each file extension.

```python
from pathlib import Path

def count_extensions(file_names):
    extensions = {}
    for file in file_names:
        ext = Path(file).suffix
        if ext in extensions:
            extensions[ext] += 1
        else:
            extensions[ext] = 1
    
    return extensions
```

---

## Block 2: Functions in Python

Functions are reusable blocks of code that perform a specific task. They help organize programs, avoid repeated code, and make logic easier to understand and test.

### Function Definitions

A function is defined using the `def` keyword.

```python
def greet():
    print("Hello!")
```

The funtion is executed only when it is called:

```python
greet()
```

General structure:

```python
def function_name():
    # Function body
```

#### Why use Functions?

Functions help you:
* divide a program into smaller parts,
* reuse code,
* avoid duplication,
* give names to specific operations,
* test parts of a program separately.

Example:

```python
def print_separator():
    print("-" * 30)
```

You can call the same function multiple times:

```python
print_separator()
print("File Analyzer")
print_separator()
```

### Parameters

Parameters allow a function to receive information from outside.

```python
def greet(name):
    print(f"Hello, {name}!")
```

Calling the function:

```python
greet("Max")

# Output
# Hello, Max!
```

Here:
* `name` is a parameter
* `"Max"` is an argument

#### Multiple Parameters

A function can have several parameters:

```python
def print_file_info(name, size):
    print(f"{name} - {size} bytes")
```

Call:

```python
print_file_info("main.py", 430)
```

The arguments are assigned based on their position:

```python
name = "main.py"
size = 430
```

### Return Values

A function can return a result using the `return` keyword.

```python
def add(number_one, number_two):
    return number_one + number_two
```

Calling the function:

```python
result = add(5, 3)

print(result)

# Output
# 8
```

The function calculates the value and sends it back to the caller.

#### Returning Collections

Functions can return lists, dictionaries, sets, tuples, or other objects.

```python
def get_supported_extensions():
    return {".py", ".md", ".json"}

extensions = get_supported_extensions()
```

#### Returning Multiple Values

A function can return multiple values:

```python
def get_smallest_and_largest(numbers):
    return min(numbers), max(numbers)

smallest, largest = get_smallest_and_largest([5, 2, 8, 1])

print(smallest)
print(largest)
```

Python returns the values as a tuple.

### Default Parameters

A default parameter has a predefined value.

```python
def format_size(size_in_bytes, decimal_places=2):
    size_in_kb = size_in_bytes / 1024
    return f"{size_in_kb:.{decimal_places}f} KB"
```

The function can be called without providing the second argument:

```python
print(format_size(2048))

# Output
# 2.00 KB
```

The default value `2` is used.

You can also provide a different value:

```python
print(format_size(2048, 1))

# Output
# 2.0 KB
```

#### Required parameters must come first

This is valid:

```python
def format_size(size_in_bytes, decimal_places=2):
    ...
```

This is not valid:

```python
def format_size(decimal_places=2, size_in_bytes):
    ...
```

#### When should you use default parameters?

Use them when:
* one value is used most of the time,
* the caller should be able to override that value,
* the function should remain convenient to call.

### Keyword Arguments

Arguments can be passed by position or by parameter name.

#### Positional arguments

```python
format_size(2048, 1)
```

Python assigns the argument based on their position:

```python
size_in_bytes = 2048
decimal_places = 1
```

#### Keyword arguments

```python
format_size(2048, decimal_places=1)
```

The parameter name is written explicitly.

You can also name every argument:

```python
format_size(
    size_in_bytes=2048,
    decimal_places=1,
)
```

#### Advantage of keyword arguments

Keyword arguments make calls easier to understand.

Compare:

```python
sort_files(files, "size", True)
```

with:

```python
sort_files(
    files,
    sort_key="size",
    reverse=True,
)
```

The second version clearly shows what `True` means.

Keyword arguments are especially useful for:
* Boolean values,
* functions with several optional parameters,
* calls where the argument meaning is not obvious,
* overriding default values.

#### Order of arguments

Positional arguments must come before keyword arguments.

Valid:

```python
format_size(2048, decimal_places=1)
```

Invalid:

```python
format_size(decimal_places=1, 2048)
```

Once you use a keyword argument, later arguments should also be keyword arguments.

### Local Variables

A variable created inside a function is usually local to that function.

```python
def calculate_total():
    total = 10 + 20
    print(total)
```

The variable `total` exists only inside the function:

```python
calculate_total()

print(total)
```

The second line causes an error because `total` is not available outside the function.

### Global Variables

A global variable is defined outside all functions.

```python
application_name = "File Analyzer"
```

It can be read inside a function:

```python
application_name = "File Analyzer"

def print_title():
    print(application_name)
```

However, modifying global variables inside functions should usually be avoided.

#### Problematic example

```python
files = []

def add_file(file_info):
    files.append(file_info)
```

The function changes data that exists outside it.

This creates a hidden dependency:

```python
add_file({"name": "main.py"})
```

You cannot fully understand the function without knowing about the global files list.

#### Better approach

Pass the required data as a parameter and return the result:

```python
def add_file(files, file_info):
    return files + [file_info]
```

Usage:

```python
files = []

files = add_file(
    files,
    {
        "name": "main.py",
        "extension": ".py",
        "size": 430,
    },
)
```

#### Avoid global mutable data

Mutable objects include:
* list
* dict
* set

Global mutable data can be changed from many places in the program.

Example to avoid:

```python
file_list = []
extension_counts = {}
supported_extensions = set()
```

if functions modify these values directly.

Prefer this:

```python
def count_files_by_extension(files):
    extension_counts = {}

    for file_info in files:
        extension = file_info["extension"]
        if extension in extension_counts:
            extension_counts[extension] += 1
        else: extension_counts[extension] = 1

    return extension_counts
```

The function receives its required information through a parameter and returns its result.

#### Constants

Global values are more  acceptable when they are intended to remain unchanged.

By convention, constants use uppercase names:

```python
BYTES_PER_KILOBYTE = 1024
DEFAULT_DECIMAL = 2

def format_size(size_in_bytes):
    size_in_kb = size_in_bytes / BYTES_PER_KILOBYTE
    return f"{size_in_kb:.{DEFAULT_DECIMAL_PLACES}f} KB"
```

Python does not technically prevent constants from being changed. Uppercase naming only communicates that the value should remain unchanged.

### Small Lambda Functions

A lambda is a small anonymous function.

Normal function:

```python
def get_file_size(file_info):
    return file_info["size"]
```

Equivalent lambda:

```python
lambda file_info: file_info["size"]
```

A lambda contains

```python
lambda parameters: returned_expression
```

It automatically returns the expression after the colon.

#### Lambda with `sorted()`

```python
sorted_files = sorted(
    files,
    key=lambda file_info: file_info["size"],
)
```

The lambda receives one file dictionary and returns its size.

Python uses that returned size as the sorting value.

#### Lambda with multiple parameters

```python
add = lambda a, b: a + b
print(add(2, 3))

# Output:
# 5
```

However, a normal function is usually clearer.

#### When should you use lambdas?

Use lambda when:
* the function is very short,
* it contains only one expression,
* it is needed only once,
* it is passed directly to another function

### Functions as Values

In Python, functions are objects. This means they can be:

* stored in variables,
* passed as arguments,
* returned from other functions,
* stored in collections.

#### Storing a function in a variable

```python
def greet(name):
    return f"Hello, {name}!"
message_function = greet
```

Notice that there are no parentheses after greet.

```python
print(message_function("Max"))

# Output:
# Hello, Max!
```

#### Function reference versus function call

This stores the function itself:

```python
operation = greet
```

This calls the function and stores its returned value:

```python
message = greet("Max")
```

The parentheses determine whether the function is called.

#### Passing a function as an argument

```python
def apply_operation(value, operation):
    return operation(value)

def double(number):
    return number * 2

result = apply_operation(5, double)

print(result)

# Output:
# 10
```

Here:

* double is passed as a value,
* operation refers to the function,
* operation(value) calls it.

#### How sorted() uses a function

The `key` argument expects a function:

```python
def get_file_size(file_info):
    return file_info["size"]

sorted_files = sorted(
    files,
    key=get_file_size,
)
```

Do not write:

```python
key=get_file_size()
```

That would call the function immediately without providing a file dictionary.

You pass the function itself:

```python
key=get_file_size
```

The lambda version works in the same way:

```python
sorted_files = sorted(
    files,
    key=lambda file_info: file_info["size"],
)
```

#### Functions in a dictionary

Functions can also be stored as dictionary values:

```python
def sort_by_name(files):
    return sorted(
        files,
        key=lambda file_info: file_info["name"],
    )


def sort_by_size(files):
    return sorted(
        files,
        key=lambda file_info: file_info["size"],
    )
sorting_options = {
    "name": sort_by_name,
    "size": sort_by_size,
}
```

Choose and call one:

```python
selected_sort_function = sorting_options["size"]

sorted_files = selected_sort_function(files)
```

This pattern can be useful when a program offers several possible operations.

### Combining these Concepts

Here is an example using several function concepts together:

```python
from pathlib import Path

def collect_files(path):
    files = []

    for item in path.iterdir():
        if item.is_file():
            file_info = {
                "name": item.name,
                "extension": item.suffix,
                "size": item.stat().st_size,
            }
            files.append(file_info)

    return files

def sort_files(files, sort_key="name", reverse=False):
    return sorted(
        files,
        key=lambda file_info: file_info[sort_key],
        reverse = reverse,
    )

def get_largest_files(files, amount=5):
    sorted_files = sort_files(
        files,
        sort_key="size",
        reverse=True,
    )

    return sorted_files[:amount]

path = Path.cwd()

files = collect_files(path)

largest_files = get_largest_files(files)
```

The example contains:
* function definitions,
* parameters,
* return values,
* default parameters,
* keyword arguments,
* local variables,
* a lambda function,
* a function call inside another function
* no global mutable data

### Common Mistakes

#### Forgetting parentheses when calling a function

```python
path = Path.cwd
```

This stores the function itself.

Correct:

```python
path = Path.cwd()
```

This calls the function and stores the returned path.

#### Modifying global lists

Avoid:

```python
files = []

def collect_file(file_info):
    files.append(file_info)
```

Prefer:

```python
def collect_file(files, file_info):
    files.append(file_info)
    return files
```

#### Using complicated lambda

Avoid:

```python
lambda file_info: file_info["size"] / 1024 if file_info["size"] > 0 else 0
```

A named function may be clearer:

```python
def get_size_in_kilobytes(file_info):
    if file_info["size"] > 0:
        return file_info["size"] / 1024

    return 0
```

### Summary

A well-designed function should usually:
* perform one clear task,
* receive required information through parameters,
* store temporary data in local variables,
* return a useful result,
* avoid changing global mutable data,
* have a clear and descriptive name.


## Block 3: Short Tasks
* `phase-1-technical-foundations\week-01-file-analyzer\exercises\day_03_functions.py`
* `phase-1-technical-foundations\week-01-file-analyzer\src\main.py`