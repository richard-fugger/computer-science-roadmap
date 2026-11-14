from pathlib import Path

from src.parser import parse_line
from src.reader import iter_lines


def main():
    file_path = Path("samples/small.log")

    try:
        for line_number, line in iter_lines(file_path):
            print(f"Row {line_number}: {line}")
            log_entry = parse_line(line)
            if log_entry is None:
                print(f"Invalid format in line {line_number}")
            else:
                print(f"Log entry generated for line {line_number}")

    except FileNotFoundError as error:
        print(error)
    except PermissionError as error:
        print(error)
    except OSError as error:
        print(error)



if __name__ == "__main__":
    main()