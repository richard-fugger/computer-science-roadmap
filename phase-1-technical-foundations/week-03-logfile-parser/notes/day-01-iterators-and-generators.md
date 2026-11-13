# Day 1 - Iterables, Iterators, and Generators

## 1. Iterables

An **iterable** is an object whose elements can be accessed one after another.

Examples:

- Lists
- Tuples
- Strings
- Dictionaries
- Sets
- Files

An iterable can provide an iterator using `iter()`.

Example:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)
```

The list is the iterable, while `iterator` is the object used to traverse its elements.

---

## 2. Iterators

An **iterator** is an object that produces values one at a time and remembers its current position.

Two important functions:

```python
iter()
```

Returns a iterator rom an iterable.

```python
next()
```

Retrieves the next value from an iterator.

Example:

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator)) # 10
print(next(iterator)) # 20
print(next(iterator)) # 30
```

Iterators implement two special methods:

- `__iter__()` - returns the iterator itself
- `__next__()` - returns the next element

Unlike a list, an iterator does not necessarily store all elements in memory.

---

## 3. StopIteration

When an iterator has no more values, `next()` raises:

```python
StopIteration
```

Example:

```python
iterator = iter([1, 2])

next(iterator)  # 1
next(iterator)  # 2
next(iterator)  # raises StopIteration
```

You can handle this exception using `try` and `except`.

A `for` loop handles `StopIteration` automatically.

---

## 4. How for Loops Work

A `for` loop internally uses the iterator protocol.

Example:

```python
for number in [10, 20, 30]:
    print(number)
```

Conceptually, Python:

1. Calls `iter()` to obtain an iterator.
2. Calls `next()` to retrieve each value.
3. Stops when `StopIteration` is raised.

This is why a `for` loop can work with lists, files, generators, and many other iterable objects.

---

## 5. Generatos and yield

A **generator** is a special kind of iterator that produces values lazily.

A generator function uses `yield` instead of returning all values at once.

Example:

```python
def numbers(limit: int):
    for value in range(limit):
        yield value
```

Usage:

```python
for number in numbers(3):
    print(number)
```

Output:

```text
0
1
2
```

Important differences:

- `return` end a function and returns a result.
- `yield` produces a value and pauses the function.
- The function resumes when the next value is requested

Calling a generator function creates a generator object. Its body does not execuet until iteration begins.

---

## 6. Generator Consumption

Generators are generally **single-use iterators**.

Example:

```python
gen = (x for x in range(3))

print(list(gen)) # [0, 1, 2]
print(list(gen)) # []
```

After a generator is exhausted, it cannot simply be restarted.

To iterate again, create a new generator.

This differs from a list, which can normally be iterated multiple times.

---

## 7. List Comprehensions vs Generator Expressions

Both provide a compact way to process values.

### List Comprehension

```python
squares = [x * x for x in range(5)]
```

Created the entire list immediately.

Result:

```python
[0, 1, 4, 9, 16]
```

### Generator Expression

```python
squares = (x * x for x in range(5))
```

Creates a generator that produces values on demand.

Main difference:

```test
List comprehension
→ computes and stores all results immediately

Generator expression
→ produces results when reauested
```

Generator expressions are especially useful when processing large amounts of data without storing every result.

---

## 8. Iterating Over Files

Python files can be iterated line by line.

Example:

```python
with open("example.log", "r", enconding="utf-8") as file:
    for line in file:
        print(line)
```

This avoids reading the entire file into memory.

Compare:

```python
file.read()
```

Reads the entire remaining file content into a string.

```python
file.readlines()
```

Reads all remaining lines into a list of strings.

---

## 9. enumerate()

`enumerate()` adds an index to each element during iteration.

Example:

```python
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names, start=1):
    print(index, name)
```

Output:

```text
1 Alice
2 Bob
3 Charlie
```

The optional `start` parameter defines the starting index.

This is especially useful for tracking line numbers while reading files.

---

## 10. Context Managers and with

A **context manager** handles entering and leaving a resource-management context.

Example:

```python
with open("example.log", "r", encoding="utf-8") as file:
    ...
```

The file is automatically closed when the `with` block exists, including when an exception occurs.

This is safer than manually opening an closing files.

When using `yield` inside a `with` block, the file stays open while the generator is paused inside that block. Closing or fully consuming the generator allows the context to finish.

---

## 11. Streaming and Memory Efficiency

Streaming means processing data incrementally instead of loading everything into memory first.

Example:

```text
Large logfile
    ↓
Read one line
    ↓
Process line
    ↓
Read next line
    ↓
Continue until finished
```

Advantages:

- lower memory consumption
- suitable for very large files
- results can be processed incrementally

A generator is useful for implementing this behaviour.

Important: Streaming does not automatically make processing faster. Its main advantage is often reduced memory usage.

---

## 12. Week 3 Project - Logfile Parser

The weekly project will analyze logfiles without loading them entirely into memory.

Initial project structure:

```text
week-03-logfile-parser/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── reader.py
├── exercises/
├── tests/
├── samples/
│   └── small.log
├── notes/
└── README.md
```

Responsibilities:

```text
exercises/
→ isolated learning exercises

reader.py
→ reading logfile lines incrementally

main.py
→ coordinating the program

samples/
→ sample logfiles for testing

tests/
→ automated tests
```

## Key Takeaways

- An iterable can provide an iterator usign `iter()`
- An iterator remembers its position and returns values using `next()`
- `StopIteration` signals that an iterator is exhausted
- `for` loops automatically use the iterator protocol
- Generator functions use `yield` to produce values lazily
- Generator objects are generally consumed onyl once
- List comprehensions create lists immediately
- Generator expressions produce values on demand
- Files can be processed incrementally using `for line in file`
- `enumerate()` provides indices during iteration
- Context managers help manage resources safely
- Streaming reduces memory usage when processing large files