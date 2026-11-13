from pathlib import Path

from src.reader import iter_lines


def main():
    file_path = Path("samples/small.log")

    try:
        for line_number, line in iter_lines(file_path):
            print(f"Row {line_number}: {line}")
    except FileNotFoundError as error:
        print(error)
    except PermissionError as error:
        print(error)
    except OSError as error:
        print(error)



if __name__ == "__main__":
    main()