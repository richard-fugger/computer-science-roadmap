import argparse
import json
from pathlib import Path
from typing import Tuple

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"
SPACER_FACTOR = 8

def resolve_output_path(path) -> Tuple[Path, str]:
     if path is None:
          return (Path.cwd() / "extension_report.json", f"{RED}Report will be saved in your current working directory{RESET}")

     output_path = Path(path)
     root = Path(output_path.anchor)

     if output_path.anchor != "" and not root.exists():
          return (Path.cwd() / "extension_report.json", f"{RED}The specified output-path cannot be reached. The report will be saved in your current working directory.{RESET}")

     if output_path.suffix != ".json":
          return (Path.cwd() / "extension_report.json", f"{RED}The ending of the specified output-path is not .json. The report will be saved in your current working directory.{RESET}")

     return (output_path, "")

def format_extension(ext):
     if ext == "":
          return "no extension"
     return ext

def sort_by_size(ext_list, desc=True):
     return sorted(
          ext_list,
          key=lambda file_info: file_info["total_size"],
          reverse=desc
     )
     
def create_report(directory) -> list[dict]:
     extension_list = []
     included_extensions = set()

     for item in directory.rglob("*"):
          if item.is_file() and item.suffix not in included_extensions:
                extension_list.append(
                     {
                          "extension": format_extension(item.suffix),
                          "count": 1,
                          "total_size": item.stat().st_size,
                     }
                )
                included_extensions.add(item.suffix)

          elif item.is_file() and item.suffix in included_extensions:
               for ext in extension_list:
                    if ext["extension"] == format_extension(item.suffix):
                         ext["count"] += 1
                         ext["total_size"] += item.stat().st_size


     return sort_by_size(extension_list)

def spacer():
     return " " * SPACER_FACTOR

def adjusted_to_title_spacer(length_input, length_title):
     factor = SPACER_FACTOR + (length_title - length_input)
     return " " * factor

def format_file_size(size):
     if size < 1024:
          return f"{size} Bytes"

     formatted_in_kb = size / 1024

     return f"{formatted_in_kb:.1f} KB"

def print_report(report):
     title_1 = "Extension"
     title_2 = "Files"
     title_3 = "Total Size"

     print(f"{title_1}{spacer()}{title_2}{spacer()}{title_3}")
     for ext in report:
          print(f"{ext["extension"]}{adjusted_to_title_spacer(len(ext["extension"]), len(title_1))}{ext["count"]}{adjusted_to_title_spacer(len(str(ext["count"])), len(title_2))}{format_file_size(ext["total_size"])}")

def export_json(report, output_path):
    try:
         with open(output_path, "w", encoding="utf-8") as file:
              json.dump(
                   report,
                   file,
                   indent=2,
                   ensure_ascii=False,
              )
              print(f"{GREEN}Exported report.{RESET}")

    except FileNotFoundError as e:
         print(f"{RED}File not found: {e}{RESET}")
    except PermissionError as e:
         print(f"{RED}Permission denied: {e}{RESET}")
    except OSError as e:
         print(f"{RED}OS error: {e}{RESET}")

     
def main():
    # Define parser
    parser = argparse.ArgumentParser(description="Analyze the extensions of a directory")
    parser.add_argument("directory", help="Directory that should be analyzed.")
    parser.add_argument("--json", action="store_true", help="Output analyzes the result as JSON")
    parser.add_argument("--output", help="Path where the JSON output should be saved.")
    args = parser.parse_args()

    # Validate directory
    directory = Path(args.directory)
    if not directory.exists():
        print(f"{RED}The specified path does not exist: {directory}{RESET}")
        return

    if directory.is_file():
            print(f"{RED}The specified path is a file instead of a directory: {args.directory}{RESET}")
            return
            
    
    if not directory.is_dir():
        print(f"{RED}Path is no valid directory: {args.directory}{RESET}")
        return

    print("Create report...\n")
    report = create_report(directory)

    print_report(report)

    if args.json:
         # Resolve output path
         (output_path, message) = resolve_output_path(args.output)
         print(message)
         print("Export report...")
         export_json(report, output_path)




if __name__ == "__main__":
    main()