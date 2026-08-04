from pathlib import Path

def collect_files(directory_path) -> list[dict]:
    files = []

    for item in directory_path.iterdir():
        if item.is_file():
            file = {
                "name": item.name,
                "size": item.stat().st_size,
            }
            files.append(file)

    return files

def get_extension(file_name: str) -> str:
    ext = Path(file_name).suffix

    if ext == '':
        ext = "no extension"

    return ext

def count_extensions(files: list[dict]) -> dict[str, int]:
    extensions = {}

    for file in files:
        extension = get_extension(file["name"])
        if extension in extensions:
            extensions[extension] += 1
        else:
            extensions[extension] = 1

    return extensions

def calculate_total_size(files: list[dict]) -> int:
    total_size = 0

    for file in files:
        size = file["size"]
        total_size += size

    return total_size

def get_largest_files(
        files: list[dict],
        limit: int = 5,
) -> list[dict]:
    sorted_files = sorted(
        files,
        key=lambda file_info: file_info["size"],
        reverse=True
    )

    return sorted_files[:limit]

def print_divider():
    print("-" * 30)

def print_extensions(extensions: dict[str, int]):
    for ext, count in extensions.items():
        print(f"{ext}: {count}")

def format_file_size(size: int, decimal_places: int=2) -> str:
    if size < 1024:
        return f"{size} Bytes"

    return f"{size / 1024:.{decimal_places}f} KB"

def print_files_with_size(files):
    for file in files:
        print(f"{file['name']} - {format_file_size(file['size'], 2)}")

def print_report(files, extensions, total_size, largest_files):
    print("File Analyzer")
    print_divider()
    print(f"Files found: {len(files)}")
    print(f"Total size: {format_file_size(total_size, 2)}")
    print_divider()
    print("Extensions:")
    print_extensions(extensions)
    print_divider()
    print("Largest Files:")
    print_files_with_size(largest_files)

def main():
    path = Path.cwd()
    files = collect_files(path)
    extensions = count_extensions(files)
    total_size = calculate_total_size(files)
    largest_files_limit_3 = get_largest_files(files, limit=3)
    print_report(files, extensions, total_size, largest_files_limit_3)

if __name__ == "__main__":
    main()
