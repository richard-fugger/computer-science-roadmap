from pathlib import Path

def collect_files(path):
    file_list = []
    for item in path.iterdir():
        if item.is_file():
            file = {
                "name": item.name,
                "extension": item.suffix,
                "size": item.stat().st_size,
            }
            file_list.append(file)
    return file_list

def get_file_extensions(files):
    extensions = set()
    for file in files:
        extensions.add(file["extension"])
    return extensions

def count_files_by_extension(files):
    extensions = {}
    for file in files:
        ext = file["extension"]
        if ext in extensions:
            extensions[ext] += 1
        else:
            extensions[ext] = 1
    return extensions

def sort_files(files, sort_key, sort_reverse):
    return sorted(files, key=lambda file: file[sort_key], reverse = sort_reverse)

def get_sliced_list(items, number):
    return items[:number]

path = Path.cwd()
file_list = collect_files(path)
print("\nCollect files:")
print(file_list)

extensions = get_file_extensions(file_list)
print("\nGet distinct file extensions:")
print(extensions)

grouped_extensions = count_files_by_extension(file_list)
print("\nGet grouped file extensions:")
print(grouped_extensions)

file_list_sorted_by_size = sort_files(file_list, "size", True)
print("\nGet files sorted by size desc:")
print(file_list_sorted_by_size)

sliced_list = get_sliced_list(file_list_sorted_by_size, 5)
print("\nGet the 5 files with highest size:")
print(sliced_list)