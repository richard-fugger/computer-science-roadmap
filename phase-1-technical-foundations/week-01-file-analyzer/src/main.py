import argparse
import json
from pathlib import Path

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def resolve_cli_output_path(output) -> Path | None:
    if output is None:
        return Path.cwd() / "analysis.json"

    output_path = Path(output)
    root = Path(output_path.anchor)

    if output_path.anchor != "" and not root.exists():
        return None

    return output_path

def collect_files(directory_path) -> list[dict]:
    """
    Recursively collects all files in a directory and returns their
    name, extension, size, and path as a list of dictionaries.
    """
    files = []

    for item in directory_path.rglob("*"):
        try:
            if item.is_file():
                file = {
                    "name": item.name,
                    "extension": item.suffix,
                    "size": item.stat().st_size,
                    "path": str(item.resolve())
                }
                files.append(file)

        except (PermissionError, OSError) as e:
            print(f"{RED}Could not read file: {item}\n{e}{RESET}")

    return files

def count_directories(directory):
    dir_count = 0
    for item in directory.rglob("*"):
        if item.is_dir():
            dir_count += 1

    return dir_count

def format_file_size(size: int, decimal_places: int = 2) -> str:
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
        limit: int,
) -> list[dict]:
    sorted_files = sorted(
        files,
        key=lambda file_info: file_info["size"],
        reverse=True
    )

    return sorted_files[:limit]

def create_report(directory, limit=5):
    files = collect_files(directory)

    return {
        "directory": str(directory.resolve()),
        "file_count": len(files),
        "directory_count": count_directories(directory),
        "total_size": calculate_total_size(files),
        "largest_files": get_largest_files(files, limit),
        "extensions": group_extensions(files),
    }

def print_files_with_size(files):
    for file in files:
        print(f"{file['name']} - {format_file_size(file['size'], 2)}")

def print_extensions(extensions: dict[str, int]):
    for ext, count in extensions.items():
            print(f"{ext}: {count}")

def print_report(report):
    print(f"\nAnalyzed directory: {report['directory']}\n")
    print(f"Files: {report['file_count']}")
    print(f"Directories: {report['directory_count']}")
    print(f"Total size: {format_file_size(report['total_size'])}\n")
    print("Largest files:")
    print_files_with_size(report["largest_files"])
    print("\nExtensions:")
    print_extensions(report["extensions"])
    print(f"{GREEN}\nSuccessfully printed report{RESET}")

def export_report_as_json(report, output_path):
    try:
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(
                report,
                file,
                indent=2,
                ensure_ascii=False,
            )

        print(f"{GREEN}Successfully exported JSON.{RESET}")

    except FileNotFoundError as e:
        print(f"{RED}File not found: {e}{RESET}")
    except PermissionError as e:
        print(f"{RED}Permission denied: {e}{RESET}")
    except OSError as e:
        print(f"{RED}OS error: {e}{RESET}")
    


def main():
    # Initialize Parser
    parser = argparse.ArgumentParser(description="Analyze a directory and optionally export the result as JSON.")
    parser.add_argument("directory", help="Directory that should be analyzed.")
    parser.add_argument("--json", action="store_true", help="Output analyzes the result as JSON")
    parser.add_argument("--output", help="Path where the JSON output should be saved.")
    parser.add_argument("--top", type=int, help="Number of largest files to display.")
    args = parser.parse_args()

    # Check directory
    directory = Path(args.directory)

    if not directory.exists():
        print(f"{RED}Path does not exits: {args.directory}{RESET}")
        return

    if directory.is_file():
        print(f"{RED}The specified path is a file instead of a directory: {args.directory}{RESET}")
        return
        

    if not directory.is_dir():
        print(f"{RED}Path is no valid directory: {args.directory}{RESET}")
        return

    print(f"Start analyzing directory: {directory}")

    # Check output path
    output_path = resolve_cli_output_path(args.output)
    if output_path is None:
        print(f"{RED}The specified path is unreachable: {args.output}{RESET}")
        return

    # check top
    if args.top is not None and args.top < 1:
        print(f"{RED}--top must be > 0.\nInput: {args.top}{RESET}")
        return

    print("Creating report...")

    # Create report
    if args.top is None:
        report = create_report(directory)
    else:
        report = create_report(directory, args.top)

    print_report(report)

    if args.json:
        export_report_as_json(report, output_path)
    

if __name__ == "__main__":
    main()
