from pathlib import Path

# 1. Write day_01_iteration.py: Create an iterator for a list, call next() multiple times, and handle the end in a controlled manner.

numbers = [1, 5, 23]
iterator = iter(numbers)

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("Last element of list was reached\n")


# 2. Write `count_up_to(n)` as a generator; check the output for `n=0`, `n=3`, and `n=5`.
def count_up_to(n):
    for number in range(n):
        yield number

gen = count_up_to(0)
print(list(gen))

gen = count_up_to(3)
print(list(gen))

gen = count_up_to(5)
print(list(gen))
print()


# 3. Read a small text file using `for line in file` and number the lines with `enumerate(..., start=1)`.

file_path = Path("samples/day_01_text_file.txt")

with open(file_path, "r", encoding="utf-8") as file:
    for index, line in enumerate(file, start=1):
        print(f"{index}, {line}", end="")
