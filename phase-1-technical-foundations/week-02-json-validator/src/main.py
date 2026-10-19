import argparse
from pathlib import Path

from src.constants import GREEN, RED, RESET
from src.exceptions import JsonValidatorError
from src.loader import load_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    args = parser.parse_args()

    try:
        print("Loading JSON file...")
        json_content = load_json(Path(args.filepath))
    except JsonValidatorError as error:
        print(f"{RED}{error}{RESET}")
        return

    print(f"{GREEN}JSON was loaded successfully.{RESET}")


if __name__ == "__main__":
    main()