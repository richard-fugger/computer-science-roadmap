# Lists, Tuples, Sets, and Dictionaries

**Start:** 02.08.2026 | 22:45

---

## Block 1: Repetition of Yesterday

How can the virtual environment for the Python project be activated?

```powershell
.\.venv\Scripts\Activate.ps1
```

How can yesterday's program be started?

```powershell
python exercises\day_01_directory_analyzer.py
```

What is the difference between an absolute path and a relative path?

* An absolute path specifies a complete location starting from the root
* A relative path specifies a location starting from the current working directory

How are changed files displayed with git?

```powershell
git status
```

---

## Block 2: Learning Data Structures

### Data Structures Overview

| Data Structure    | Syntax             | Ordered   | Mutable       | Duplicates    | Typical Use                                |
--------------------|--------------------|-----------|---------------|---------------|--------------------------------------------|
List                | [1, 2, 3]          | Yes       | Yes           | Yes           | An ordered collection of values            |
Tuple               | (1, 2, 3)          | Yes       | No            | Yes           | A fixed collection of related values       |
Set                 | {1, 2, 3}          | No        | Yes           | No            | Unique values and fast membership check    |
Dictionary          | {"name": "Max"}    | Yes       | Yes           | Keys: No      | Key-value mappings                         |

### Lists

A list is an ordered and mutable collection.

```python
fruits = ["apple", "banana", "orange"]
```

You can access elements by their indexes:

```python
print(fruits[0]) # apple
print(fruits[1]) # banana
```

List indexes start at 0.

#### Modifying Lists

```python
fruits.append("pear")
fruits.remove("banana")
fruits[0] = "strawberry"

print(fruits)

# Output:
# ['strawberry', 'orange', 'pear']
```

#### List Use Cases

Use a list when:
* the order of the elements matters,
* duplicate values are allowed,
* elements should be added or removed later,
* you want to access elements by position.

#### Important List Methods

```python
numbers = [10, 20, 30]

numbers.append(40)          # Add an element at the end
numbers.insert(1,15)        # Insert an element at a specific position
numbers.remove(20)          # Remove a specific value
last_number = numbers.pop()  # Remove and return the last element
numbers.sort()              # Sort the list
numbers.reverse()           # Reverse the order
```

### Tuples
A tuple is similar to a list, but it cannot be modified after it has been created.

```python
position = (10, 20)
```

You can also access tuple values by index:

```python
print(position[0])  # 10
print(position[1])  # 20
```

The following does not work:

```python
position[0] = 30
```

This causes an error because tuples are immutable.

#### Tuple Use Cases

Use a tuple when:
* multiple values belong together,
* the values should not be changed,
* each position has a fixed meaning,
* a function should return multiple values.

#### Tuple Unpacking

An important use case for tuples is called unpacking:

```python
screen_size = (1920, 1080)

width, height = screen_size

print(width)  # 1920
print(height)  # 1080
```

A function can therefore return multiple values:

```python
def get_min_and_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_and_max([5, 2, 9, 4])

print(minimum)  # 2
print(maximum)  # 9
```

Technically, the function returns a tuple:

```python
result = get_min_and_max([5, 2, 9, 4])

print(result)       # (2, 9)
print(type(result)) # <class 'tuple'>
```

#### Tuple with one element

There is one special rule:

```python
value = (5)
```

This is not a tuple. It is an integer.

A tuple with one element requires a comma:

```python
value = (5,)

print(type(value))  # <class 'tuple'>
```

The comma creates the tuple, not the parentheses

### Sets

A set is a collection of unique values.

```python
numbers = {1, 2, 3}
```

Duplicate values are removed automatically:

```python
numbers {1, 2, 2, 3, 3, 3}

print(numbers)

# Output:
# {1, 2, 3}
```

You should not rely on the order of elements in a set. You also cannot access set elements by index:

```python
numbers[0]
```

This does not work.

#### Set Use Cases

Use a set when:
* every value should appear only once,
* you want to remove duplicates,
* you frequently check whether a value exists,
* you want to perform mathematical set operations.

##### Remove Duplicates

```python
names = ["Anna", "Max", "Anna", "Lisa", "Max"]

unique_names = set(names)

print(unique_names)

# Possible Output
# {'Anna', 'Max', 'Lisa'}

# You can convert it back into a list:
unique_names_list = list(set(names))
```

However, you should not rely on the original order being preserved.

##### Fast Membership Checks

```python
allowed_extensions = {".py", ".md", ".json"}

extension = ".py"

if extension in allowed_extensions:
    print("File type is allowed.")
```

For membership checks, a set is usually more suitable than a list:

```python
extension in allowed_extensions
```

Searching in a set is usually very fast. With a list, Python may need to check every element one after another.

#### Set Operations

Sets can be used like mathematical sets.

```python
python_skills = {"functions", "lists", "classes"}
required_skills = {"lists", "classes", "testing"}
```

##### Intersection

Values that appear in both sets:

```python
shared_skills = python_skills & required_skills

print(shared_skills)

# Output
# {'lists', 'classes'}
```

##### Union

All values from both sets:

```python
all_skills = python_skills | required_skills
```

#### Important Set Methods

```python
skills = {"lists", "tuples"}

skills.add("sets")
skills.remove("lists")
skills.discard("dictionaries")
```

The difference between `remove()` and `discard()` is important.

This causes an error if the value does not exist:

```python
skills.remove("unknown")
```

This does not cause an error:

```python
skills.discard("unknown")
```

#### Empty Set

This is not an empty set:

```python
empty = {}
```

It creates an empty dictionary.

Create an empty set like this:

```python
empty_set = set()
```

### Dictionaries

A dictionary stores values as key-value pairs.

```python
user = {
    "name": "Max",
    "age": 19,
    "city": "Vienna",
}
```

Instead of using a numerical index, you access values using their keys:

```python
print(user["name"]) # Max
print(user["city"]) # Vienna
```

#### Dictionary Use Cases

Use a dictionary when:
* each value needs a clear name,
* you want to store information about an object,
* you want to find values using keys,
* you want to represent data similar to JSON.


#### Modifying a Dictionary

```python
user =  {
    "name": "Max",
    "age": 19,
}

user["city"] = "Vienna"
user["age"] = 20

del user["city"]
```

#### Accessing Values Safely

This causes an error if the key does not exist:

```python
print(user["email"])
```

You can use `get()` to access the value safely:

```python
email = user.get("email")

print(email) # None
```

You can also provide a default value:

```python
email = user.get("email", "No email available")
```

#### Iteration over a Dictionary

##### Keys Only

```python
for key in user:
    print(key)
```

You can also write explicitly:

```python
for key in user.keys():
    print(key)
```

##### Values Only

```python
for value in user.values():
    print(value)
```

##### Keys and Values

```python
for key, value in user.items():
    print(f"{key}: {value}")
```

The `items()` method provides a tuple during each iteration.
The tuple is unpacked directly.


## Block 3: Short Tasks
* `phase-1-technical-foundations\week-01-file-analyzer\exercises\day_02_data_structure_functions.py`
* `phase-1-technical-foundations\week-01-file-analyzer\src\main.py`

**End:** 03.08.2026 | 02:30