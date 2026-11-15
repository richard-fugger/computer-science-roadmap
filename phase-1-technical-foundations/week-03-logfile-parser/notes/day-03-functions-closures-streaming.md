# Day 3 - Functions as Values, Closures, and Streaming

## 1. Functions as Values

In Python, functions are **first-class objects**.

This means a function can be:

- assigned to a variable
- passed as an argument
- returned from another function
- stored in a collection

Example:

```python
def is_even(number: int) -> bool:
    return number % 2 == 0

predicate = is_even

print(predicate(4)) # True
```

Important difference:

```python
predicate = is_even     # Store function reference
predicate = is_even(4)  # Store function result
```

---

## 2. Higher-Order Functions

A **higher-order function** is a function that accepts another function as an argument or returns a function.

Example:

```python
def apply_operation(value, operation):
    return operation(value)

def double(number):
    return number * 2

result = apply_operation(5, double)
```

Here, `apply_operation()` receives `double` as a function argument.

This allows behaviour to be passed dynamically instead of hardcoding it.

---

## 3. Callable

`Callable` describes the expected parameters and return type of a callable object.

```python
from collection.abc import Callable
```

Example:

```python
def apply_operation(
    value: int,
    operation: Callable[[int], int]
) -> int:
return operation(value)
```

Meaning:

```text
Callable[[int], int]
         ↓      ↓
     Parameter  Return type
```

For the logfile parser, a filter could have the type:

```python
Callable[[LogEntry], bool]
```

It receives a `LogEntry` and returns `True` or `False`.

---

## 4. Closures

A **closure** is a function that retains access to variables from its enclosing scope, even after the outer function has finished.

Example:

```python
def make_prefix_filter(prefix: str):
    def matches(text: str) -> bool:
        return text.startswith(prefix)
    
    return matches
```

Usage:

```python
starts_with_err = make_prefix_filter("ERR")

print(start_with_err("ERROR")) # True
print(starts_with_err("INFO")) # False
```

The inner function remembers the variable `prefix`.

Conceptually:

```text
make_prefix_filter("ERR")
       ↓
Creates matches()
       ↓
matches() retains access to prefix
       ↓
Function can be called later
```

Closures are useful for creating cinfigurable functions without repeadetly passing the same configuration.

**Important:** Not every function needs a closure. Normal functions are often simpler.

---

## 5. Closures vs. Normal Functions

A normal function receives all required values through its parameters.

```python
def starts_with(text: str, prefix: str) -> bool:
    return text.startwith(prefix)
```

A closure remembers configuration from its enclosing scope.

```python
starts_with_err = make_prefix_filter("ERR")
start_with_err("ERROR")
```

The difference is where the configuration comes from:

```text
Normal function
→ configuration passed on each call

Closure
→ configuration retained from enclosing scope
```

---

## 6. Generator Expressions

A generator expression produces values lazily.

Example:

```python
numbers = [1, 2, 3, 4]

squares = (number ** 2 for number in numbers)
```

Values are calculated when requested:

```python
next(sqaures) # 1
next(squares) # 4
```

A generator expression can also be passed directly to functions such as `sum()`:

```Python
total = sum(number ** 2 for number in numbers)
```

No imediate list of squared numbers is created.

---

## 7. List Comprehension vs Generator Expression

### List Comprehension

```python
squares =  (x ** 2 for x in range(5))
```

- evaluates all elements immediately
- stores results in a list
- can be iterated multiple times

### Generator Expression

```python
squares = (x ** 2 for x in range(5))
```

- evaluates elements lazily
- does not store the complete result
- is normalle consumed once

**Main difference:** List store results; generators produce them when requested.

---

## 8. Context Managers

A **context manager** controls the setup and cleanup of a resource.

The `with` statement is commonly used for file operations.

```python
with open("example.log", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
```

Advantages:

- automatically closes files when leaving the block
- handles cleanup even when exceptions occur
- avoids manually calling `file.close()`

Context managers use two special methods:

```python
__enter__()
```

Called when entering the context.

```python
__exit__()
```

Called when leaving the context, including during exception handling.

---

## 9. Context Managers with Generators

When a generator uses `yield` inside a `with` block, the resource remains open while execution is paused inside that block.

Example:

```python
def read_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            yield line
```

Important behaviour:

1. Calling `read_lines()` creates a generator.
2. The file is opened when iteration begins.
3. Each `yield` pauses execution while the file remains open.
4. Once iteration finishes normally, the `with` block closes the file.

**Caution:** If iteration stop early, the generator may remain suspended with the file open. Explicitely closing the generator ensures cleanup.

---

## 10. Streaming Pipelines

A **streaming pipeline** processes data incrementally through multiple through multiple processing steps.

For the logfile parser:

```text
Logfile
    ↓
reader.iter_lines()
    ↓
(line_number, line_text)
    ↓
parser.parse_line()
    ↓
LogEntry | None
    ↓
Further processing
```

Each log line is read and parsed independently.

Advantages:

- low memory usage
- suitable for large logfiles
- clear separation of responsibilities
- processing can begin before the entire file is read

Avoid:

```python
list(iter_lines(path))
```

in the actual streaming pipeline because it loads all generated entries into memory.

---

## Key Takeaways

- Functions are first-class objects in Python
- Higher-order functions accept or return other functions
- `Callable` describes a callable's parameter and return types
- Closures retain access to variables from their enclosing scope
- Closures are useful for configurable behaviour but are not always necessary
- Generator expressions produce values lazily
- List comprehensions create complete lists immediately
- Context managers handle resource setup and cleanup
- `__enter__()` ans `__exit__()` implement thr context manager protocol
- Generators can keep files open while paused inside a `with` block
- Streaming pipelines process data incrementally without loading everything into memory
- Integration tests verify that multiple modules work together