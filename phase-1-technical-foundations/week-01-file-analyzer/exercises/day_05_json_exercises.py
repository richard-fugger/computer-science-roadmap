import json
from pathlib import Path


def analyse_dir(dir):
    if not dir.is_dir():
        return False

    file_count = 0
    dir_count = 0
    total_size = 0

    for item in dir.rglob("*"):
        if item.is_file():
            file_count += 1
            total_size += item.stat().st_size

        elif item.is_dir():
            dir_count += 1

    return {
        "directory": str(dir),
        "file_count": file_count,
        "directory_count": dir_count,
        "total_size": total_size,
    }

def export_as_json(content, output_path):    
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            content,
            file,
            indent = 2,
            ensure_ascii = False,
        )
        return "export_as_json: success"

def import_as_json(path):
    if not path.exists():
        return None
    
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def are_equal(old, new):
    return old == new

def get_files(dir):
    files = []

    for item in dir.rglob("*"):
        if item.is_file():
            files.append(
                {
                    "name": item.name,
                    "size": item.stat().st_size,
                }
            )

    return files

def sort_files(files, desc = True):
    sorted_files = sorted(
        files,
        key=lambda file_info: file_info["size"],
        reverse = desc
    )

    return sorted_files
    
def get_largest_files(dir, limit):
    files = get_files(dir)
    return sort_files(files)[:limit]

def add_files_to_json(dir, limit, output_path):
    if not dir.is_dir():
        return f"{dir} is not a directory."

    if not output_path.exists():
        return f"{output_path} is not a valid path."

    if limit < 1:
        return f"Limit must be higher than 0. Currently: {limit}"
    
    file_list = get_largest_files(dir, limit)

    with open(output_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    data["files"] = file_list

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=2,
            ensure_ascii=False
        )

    return f"Files have successfully been appended to {output_path}"

def get_extension(file_name):
    ext = Path(file_name).suffix

    if ext == '':
        ext = "no extension"

    return ext

def group_extensions(files):
    extensions = {}

    for file in files:
        extension = get_extension(file["name"])
        if extension in extensions:
            extensions[extension] += 1
        else:
            extensions[extension] = 1

    return extensions

def format_extensions(files):
    ext_list = []

    extensions = group_extensions(files)

    for ext, count in extensions.items():
        ext_list.append(
            {
                "name": ext,
                "count": count,
            }
        )

    return ext_list

def add_extensions_to_json(dir, output_path):

    if not dir.is_dir():
        return f"{dir} is not a directory."

    if not output_path.exists():
        return f"{output_path} is not a valid path."

    extensions = format_extensions(get_files(dir))

    with open(output_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    data["extensions"] = extensions

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=2,
            ensure_ascii=False
        )
    


def main():
    # Define constants
    DIR = Path("D:/nutrition-tracker/nutrition_tracker")
    OUTPUT_PATH = Path("phase-1-technical-foundations/week-01-file-analyzer/output/05-day/analysis.json")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Analyse dir
    analysis = analyse_dir(DIR)
    print(analysis)

    # Export analyses as JSON
    success = export_as_json(analysis, OUTPUT_PATH)
    print(f"Export success: {success}")

    # Import JSON
    loaded_analysis = import_as_json(OUTPUT_PATH)
    print(loaded_analysis)

    # Check if they are equal
    equal = are_equal(analysis, loaded_analysis)
    print(f"Equal: {equal}")

    # Append file-details to existing JSON
    message = add_files_to_json(DIR, 5, OUTPUT_PATH)
    print(message)

    # Append extensions + count to existing JSON
    add_extensions_to_json(DIR, OUTPUT_PATH)

    

if __name__ == "__main__":
    main()
