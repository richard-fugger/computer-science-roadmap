from collections.abc import Callable
from pathlib import Path


def print_divider() -> None:
    print("----------------------------")

# 1. Write a function `apply_filter(values, predicate)` that returns only the matching values. Pass in two different filter functions.

def apply_filters(values: list [int], predicate: Callable[[int], bool]) -> list[int]:
    return [x for x in values if predicate(x)]

def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            return False
    return True

def is_even(value: int) -> bool:
    return value % 2 == 0

values = [1, 2, 3, 4, 5, 36, 37, 100]
even = apply_filters(values, is_even)
prime = apply_filters(values, is_prime)

def print_numbers(values: list[int]) -> None:
    for v in values:
        print(v)

print("Even:")
print_numbers(even)
print_divider()
print("Prime:")
print_numbers(prime)
print_divider()


# 2. Create a filter for strings that begin with a chosen prefix, using a closure.

def make_prefix_filter(filter: str):
    def starts_with_präfix(text: str):
        return text.startswith(filter)
    return starts_with_präfix

start_with_in = make_prefix_filter("IN")

print(start_with_in("INFO"))
print(start_with_in("ERROR"))
print_divider()


# 3. Calculate the sum of squares using a generator expression, without creating an intermediate list.

total = sum(x**2 for x in range(5))
print(total)
print_divider()

# 4. Open a text file using `with`, read only the first two lines, and check when it gets closed.

def read_file(path: Path):
    file = None
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                for line in file:
                    yield line
            finally:
                print("File closed:", file.closed)
    finally:
        if file is not None:
            print("After with:", file.closed)


text_file = Path("samples/day_01_text_file.txt")

gen = read_file(text_file)
print(next(gen), end="")
print(next(gen), end="")
gen.close()
