# Day 2 - Regular Expressions and Log Parsing

## 1. What are Regular Expressions?

A **regular expression (regex)** is a pattern used to search, match, or extract information from text.

Python provides the built-in `re` module.

Common use cases:

- validating text formats
- extracting IDs and dates
- searching for specific patterns
- parsing structured log entries

Example:

```python
import re

pattern = re.compile(r"\d+")
match = pattern.search("User ID: 482")

print(match.group()) # 482
```

---

## 2. Basic Regex Syntax

| Syntax | Meaning | Example |
|---|---|---|
| `\d` | Digit (0-9 and other Unicode digits) | `\d{4}` |
| `\w` | Word character | `\w+` |
| `\s` | Whitespace | `\s+` |
| `.` | Any character except newline by default | `a.b` |
| `*` | Zero or more repetitions | `a*` |
| `+` | One or more repetitions | `a+` |
| `?` | Zero or one occurrence | `a?` |
| `{n}` | Exactly n repetitions | `\d{4}` |
| `[A-Z]` | Character range | `[A-Z]+` |
| `^` | Start of string | `^ERROR` |
| `$` | End of string | `ERROR$` |
| `(...)` | Capture group | `(INFO\|ERROR)` |
| `(?P<name>...)` | Named capture group | `(?P<id>\d+)` |

Special characters can be escaped with `\`.

Example:

```python
r"\[auth\]"
```

matches the literal text `[auth]`.

---

## 3. Raw Strings

Regex patterns should usually be written as raw strings:

```python
r"\d+"
```

The prefix `r` prevents Python from interpreting most backslash sequences before regex engine receives them.

This makes patterms easier to read and avoids escaping problems.

---

## 4. Compiling Patterns

`re.compile()` creates a reusable regex pattern object.

```python
pattern = re.compile(r"\d+")
```

The pattern can then be used multiple times:

```python
pattern.search("ID: 123")
pattern.search("ID: 456")
```

This is useful when processing thousands of log lines with the same pattern.

---

## 5. search(), match(), and fullmatch()

### search()

Searches for a match anywhere in the string.

```python
pattern = re.compile(r"\d+")

pattern.search("ID: 123")
```

Finds: `123`.

### match()

Checks for a match at the beginning of the string.

```python
pattern.match("123 abc")
```

Matches `123`.

### fullmatch()

Requires the entire string to match the pattern.

```python
pattern.fullmatch("123")
```

Matches successfully.

```python
pattern.fullmatch("123 abc")
```

Returns `None`.

**For validating complete log lines, `fullmatch()` is usually the best choice.**

---

## 6. Capture Groups

Parentheses allow parts of a match to be extracted.

```python
pattern = re.compile(r"ID=(\d+)")
match = pattern.search("ID=482")

if match is not None:
    print(match.group(0)) # ID=482
    print(match.group(1)) # 482
```

Important:

- `group(0)` returns the entire match.
- `group(1)` returns the first captured group.
- `group(2)` returns the second captured group.

---

## 7. Named Capture Groups

Named groups make extracted values easier to access.

```python
pattern = re.compile(r"ID=(?P<id>\d+)")
match = pattern.search("ID=482")

if match is not None:
    print(match.group("id"))
```

Named groups are especially useful for structured data such as:

```text
timestamp
level
component
message
```

Multiple named groups can also be retrieved as a dictionary:

```python
match.groupdict()
```

---

## 8. Handling missing Matches

Regex operations return `None` when no match is found.

Always check before accessing groups:

```python
match = pattern.search(text)

if match is None:
    print("No match found")
else:
    print(match.group())
```

Calling `.group()` on `None` would raise an `AttributeError`.

For a parser, an unsuccessful match can indicate an invalid log line.

---

## 9. Greedy Matching

The pattern:

```regex
.*
```

matches zero or more characters and is **greedy**.

This means it tries to match as much text as possible.

Example:

```python
pattern = re.compile(r"\[.*]")
```

For:

```text
[auth] message [error]
```

the match spans from the first `[` to the last `]`.

A more restrictive pattern is often safer:

```python
r"\[[^\]]+\]"
```

This matches bracketed text without crossing a closing bracket.

Use precise patterns when validating structured input.

---

## 10. Parsing Dates with datetime

Regex validated the textual structure of a date, but not wheter the date actually exists.

For example:

```text
2026-02-30
```

matches a `YYYY-MM-DD` pattern but is not a valid date.

Python provides:

```python
from datetime import datetime
```

Example:

```python
date = datetime.strptime(
    "2026-08-15",
    "%Y-%m-%d"
)
```

Common format codes:

| Code | Meaning |
|---|---|
| `%Y` | Four-digit year |
| `%m` | Month |
| `%d` | Day |
| `%H` | Hour |
| `%M` | Minute |
| `%S` | Second |

Invalid dates or incompatible formats raise `ValueError`.

Therefore, parsing should distinguish:

```text
Regex matches
→ text has the expected structure

datetime.strptime() succeeds
→ date/time is valid
```

---

## Key Takeaways

- Regex patterns describe structures within text
- `re.compile()` created reusable patterns
- `search()` looks anywhere in a string
- `match()` checks from the beginning
- `fullmatch()` requires the entire string to match
- Capture groups extract parts of matches text
- Named groups improve readability
- Missing mathces return `None`
- Greedy patterns like `.*` can accept too much text
- Raw strings make regex patterns easier to write
- `datetime.strptime()` validates and converts date/time strings