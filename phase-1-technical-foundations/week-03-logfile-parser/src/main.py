from pathlib import Path

from src.pipeline import iter_parsed_lines


def main():
    file_path = Path("samples/small.log")

    try:
        for line_number, parsed_line in iter_parsed_lines(file_path):
            if parsed_line is None:
                print(f"Invalid log in line {line_number}")
            else:
                print(f"Valid log in line {line_number}")

    except FileNotFoundError as error:
        print(error)
    except PermissionError as error:
        print(error)
    except OSError as error:
        print(error)



if __name__ == "__main__":
    main()