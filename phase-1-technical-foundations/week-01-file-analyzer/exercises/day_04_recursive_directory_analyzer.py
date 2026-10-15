from pathlib import Path


def path_is_directory(path: Path) -> bool:
    if not path.exists():
        return False

    return path.is_dir()


def get_files_recursive(path: Path) -> list[dict]:
    files = []

    if not path_is_directory(path):
        return []

    for item in path.rglob("*"):
        if item.is_file():
            file = {
                "name": item.name,
                "size": item.stat().st_size,
                "absolute": item.resolve(),
            }

            files.append(file)

    return files

def get_subdirectories_recursive(path: Path) -> list[dict]:
    sub_directories = []

    if not path_is_directory(path):
        return []

    for item in path.rglob("*"):
        if item.is_dir():
            dir = {
                "name": item.name,
                "absolute": item.resolve(),
            }

            sub_directories.append(dir)

    return sub_directories

def calculate_total_size(path: Path) -> float:
    if not path_is_directory(path):
        return 0

    size = 0

    for item in path.rglob("+"):
        if item.is_file():
            file_size = item.stat().st_size
            size += file_size

    return size

def format_files(files: list[dict]) -> str:
    formatted_files = ''

    for file in files:
        formatted_files += f"- Name: {file['name']}\n- Size: {file['size']}\n- Absolute: {file['absolute']}\n\n"

    return formatted_files

def format_directories(directories: list[dict]) -> str:
    formatted_dirs = ''

    for dir in directories:
        formatted_dirs += f"- Name: {dir['name']}\n- Absolute: {dir['absolute']}\n\n"

    return formatted_dirs

def create_divider() -> str:
    return "-"*30

def create_directory_summary_as_txt(
        summary_path: Path,
        file_name: str,
        analyzed_path: Path,
        ):

    output_path = summary_path / file_name
    
    with output_path.open("w", encoding="utf-8") as file:
        file.write(f"Analyzed Directory: {analyzed_path}\n\n")
        file.write(create_divider())
        file.write("\n\nFiles:\n")
        file.write(format_files(get_files_recursive(analyzed_path)))
        file.write(create_divider())
        file.write("\n\nDirectories:\n")
        file.write(format_directories(get_subdirectories_recursive(analyzed_path)))
        file.write(create_divider())
        file.write(f"\n\nTotal size: {calculate_total_size(analyzed_path)} Bytes")
    
def main():
    path = Path.cwd()
    create_directory_summary_as_txt(
        path,
        "directory_summary.txt",
        Path("D:/other/ait"),
    )

if __name__ == "__main__":
    main()