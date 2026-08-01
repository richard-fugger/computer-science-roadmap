from pathlib import Path

def format_file_size(size_in_bytes):
    if size_in_bytes < 1024:
        return f"{size_in_bytes} Bytes"

    size_in_kb = size_in_bytes / 1024
    return f"{size_in_kb:.1f} KB"

print("Starting Directory Analyzer")

directory_path = Path.cwd()
print(f"Directory: {Path.cwd().name}\n")

for item in directory_path.iterdir():
    if item.is_file():
        file_name = item.name
        file_size = item.stat().st_size
        formatted_file_size = format_file_size(file_size)

        print(f"{file_name} - {formatted_file_size}")