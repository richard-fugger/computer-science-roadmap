# Day 4 - Log Analytics and Treaming Aggregation

## 1. What is Aggregation?

**Aggregation** means combining individual dara entries into summarized results.

Instead of storing every log entry, we calculate statistics such as:

- Total number of lines
- Number of valid and invalid entries
- Number of entries per log level
- Number of entries per component
- Most frequent error messages
- Earliest and latest error timestamps

For large logfiles, these statistics should be updated while reading the file.

---

## 2. Streaming Aggregation

Streaming aggregation processes entries **one at a time**, without collecting the complete input.

Conceptual flow:

```text
Logfile
    ↓
Read one line
    ↓
Parse line
    ↓
Update statistics
    ↓
Continue with next line
    ↓
Return final report
```

Advantages:

- Reduced memory consumption
- Suitable for large files
- Only one pass through the input is required

Avoid consuming the entire generator before analyzing it:

```python
entries = list(iter_parsed_lines(path))
```

Instead, process each entry directly during iteration.

**Important:** A generator is consumed as it is iterated. Iterating over the same exhausted generator again produces no values.

---

## 3. Counting with Counter

`Counter` is a dictionary subclass designed for counting hashable values.

```python
from collections import Counter

levels = Counter()

levels["ERROR"] += 1
levels["INFO"] += 1
levels["ERROR"] += 1
```

Result:

```python
Counter({"ERROR": 2, "INFO": 1})
```

Accessing a missing key returns `0`:

```python
levels["WARNING"] # 0
```

### most_common()

Returns the most frequent elements and their counts.

```python
messages = Counter({
    "Invalid token": 5,
    "Connection lost": 3,
    "Timeout": 2
})

messages.most_common(2)
```

Result:

```python
[
    ("Invalid token", 5),
    ("Connection lost", 3)
]
```

Useful for identifying frequently occuring errors.

---

## 4. Working with datetime

Python supports comparisons between `datetime` objects.

```python
from datetime import datetime

first = datetime(2026, 8, 15, 10, 20)
second = datetime(2026, 8, 15, 10, 30)

print(first < second)  # True
```

`min()` and `max()` find the earliest and latest timestamp:

```python
earliest = min(first, second)
latest = max(first, second)
```

For streaming aggregation, the minimum and maximum can be updated whenever a new error is encountered.

**Important:** The earliest error timestamp is not necessarily the first error encountered in the file.

For empty input, avoid calling `min()` or `max()` on an empty collection without a default.

---

## 5. Report Data Model

A report should contain the aggregated results, independently of how they are displayed.

Required fields:

| Field | Meaning |
|---|---|
| `total_lines` | All lines, including invalid ones |
| `valid_entries` | Successfully parsed entries |
| `invalid_lines` | Lines that could not be parsed |
| `by_level` | Counts per log level |
| `by_component` | Counts per component |
| `top_error_messages` | Most common ERROR/CRITICAL messages |
| `first_error` | Earliest error timestamp |
| `last_error` | Latest error timestamp |
| `error_time_samples` | Optional: first 10 error timestamps in file order |

A 'LogReport'  dataclass is one possible way to represent this data.

For an empty logfile:

```text
total_lines   = 0
valid_entries = 0
invalid_lines = 0
first_error   = None
last_error    = None
```

Counters and message collections should be empty.

---

## 6. Memory Usage and Counter Limitations

Streaming avoids storing all raw lines or LogEntry objects.

However, aggregation still requires some memory.

For example:

```python
error_message = Counter()
```

If every error message is unique, the Counter may grop significantly.

Therefore:

**Streaming dies not automatically guarantee constant memory usage.**

Memory consumption depends on which information the application retains.

For Version 1, storing counters for distinct messages and components is acceptable.

---

## 7. Parser Errors vs. Runtime Errors

### Parser Failure

A line does not match the expected log format.

Example:

```text
invalid-log-line
```

Expected behaviour:

```python
parse_line(line) # None
```

Ther analyzer counts it as an invalid line and continues.

### Runtime Error

An operation fails unexpectedle or cannot complete.

Examples:

- File does not exist
- Missing file permissions
- File cannot be read

Such errors generally require exception handling.

**Key distinction:**

```text
Invalid input format
→ Expected validation failure

Failed operation
→ Exception that must be handled appropriately
```

---

## Key Takeaways

- Aggregation summarizes individualentries into statistics
- Streaming aggregation processes each entry once
- `Counter` is useful for frequencies and `most_common`
- `datetime` objects can be compared chronologically
- Earliest/latest timestamps differ from first/last file occurence
- A report model separates data from presentation
- Analytics should not depend on terminal output
- Invalid lines must be included in the total line count
- Parser failures and runtime exceptions are different
- Streaming saves memory, but growing counters still consume memory