import json
from pathlib import Path


def collect_files(directory_path) -> list[dict]:
    """
    Recursively collects all files in a dictionary and returns their
    name, extension, size, and path as a list of dictionaries.
    """
    files = []

    for item in directory_path.rglob("*"):
        if item.is_file():
            file = {
                "name": item.name,
                "extension": item.suffix,
                "size": item.stat().st_size,
                "path": str(item.resolve())
            }
            files.append(file)

    return files

def count_directories(directory):
    dir_count = 0
    for item in directory.rglob("*"):
        if item.is_dir():
            dir_count += 1

    return dir_count

def format_file_size(size: int, decimal_places: int=2) -> str:
    if size < 1024:
        return f"{round(size, decimal_places)} Bytes"

    return f"{round(size / 1024, decimal_places)} KB"

def calculate_total_size(files: list[dict]) -> int:
    total_size = 0

    for file in files:
        size = file["size"]
        total_size += size

    return total_size

def format_extension_name(extension: str) -> str:
    ext = extension
    if extension == '':
        ext = "no extension"

    return ext

def group_extensions(files: list[dict]) -> dict[str, int]:
    extensions = {}

    for file in files:
        extension = format_extension_name(file["extension"])
        if extension in extensions:
            extensions[extension] += 1
        else:
            extensions[extension] = 1

    return extensions

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

def create_report(directory):
    files = collect_files(directory)

    return {
        "directory": str(directory.resolve()),
        "file_count": len(files),
        "directory_count": count_directories(directory),
        "total_size": calculate_total_size(files),
        "largest_files": get_largest_files(files),
        "extensions": group_extensions(files),
    }

def print_files_with_size(files):
    for file in files:
        print(f"{file['name']} - {format_file_size(file['size'], 2)}")

def print_extensions(extensions: dict[str, int]):
    for ext, count in extensions.items():
            print(f"{ext}: {count}")

def print_report(report):
    print(f"Analyzed directory: {report['directory']}\n")
    print(f"Files: {report['file_count']}")
    print(f"Directories: {report['directory_count']}")
    print(f"Total size: {format_file_size(report['total_size'])}\n")
    print("Largest files:")
    print_files_with_size(report["largest_files"])
    print("\nExtensions:")
    print_extensions(report["extensions"])
    print("\nPrinting report finished.")

def export_report_as_json(report, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            report,
            file,
            indent=2,
            ensure_ascii=False,
        )

    print("Successfully exported JSON.")


def main():
    # Define constants
    DIRECTORY = Path("D:/nutrition-tracker/nutrition_tracker")
    OUTPUT_PATH = Path("phase-1-technical-foundations/week-01-file-analyzer/output/05-day-main-project-report.json")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    if not DIRECTORY.is_dir():
        print(f"Directory does not exist {DIRECTORY}")

    report = create_report(DIRECTORY)

    print_report(report)
    export_report_as_json(report, OUTPUT_PATH)
    

if __name__ == "__main__":
    main()
