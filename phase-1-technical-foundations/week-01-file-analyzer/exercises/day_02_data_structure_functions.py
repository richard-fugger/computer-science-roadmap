# Task 1: Remove duplicates
names = ["a.txt", "b.txt", "a.txt", "c.txt"]

names_unique = set(names)
print("Task 1: Remove duplicates")
print(f"Raw list: {names}")
print(f"Unique set: {names_unique}")

# Task 2: Group and count file extensions
from pathlib import Path
files = ["main.py", "test.py", "README.md", "data.json"]
extensions = {}

for file in files:
    extension = Path(file).suffix
    # print(extension)
    if extension in extensions.keys():
        extensions[extension] += 1
    else:
        extensions[extension] = 1

print("\nTask 2: Group and count file extensions")
print(f"Initial list: {files}")
print(f"Grouped and counted extensions {extensions}")

# Task 3: Sort files
file_list = []
path = Path.cwd()

for item in path.iterdir():
    if(item.is_file()):
        file = {
            "name": item.name,
            "size": item.stat().st_size
        }
        file_list.append(file)


def sort_files(files, sort_key, sort_reverse = False):
    return sorted(files, key=lambda file: file[sort_key], reverse = sort_reverse)
        

print("\nTask 3: Sort files")

files_list_sorted_by_names = sort_files(file_list, "name")
print("\nSort by name:")
print(files_list_sorted_by_names)

files_list_sorted_by_size_asc = sort_files(file_list, "size")
print("\nSort by size ASC:")
print(files_list_sorted_by_size_asc)

files_list_sorted_by_size_desc = sort_files(file_list, "size", True)
print("\nSort by size DESC:")
print(files_list_sorted_by_size_desc)