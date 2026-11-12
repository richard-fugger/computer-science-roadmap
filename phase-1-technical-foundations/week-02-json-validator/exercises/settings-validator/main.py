import argparse
import json
from pathlib import Path

from loader import load_json
from validator import validate_document

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        data = load_json(Path(args.file))
    except FileNotFoundError as error:
        print(f"{RED}{error}{RESET}")
        return 1
    except PermissionError as error:
        print(f"{RED}{error}{RESET}")
        return 1
    except json.JSONDecodeError as error:
        print(f"{RED}{error}{RESET}")
        return 1
    except OSError as error:
        print(f"{RED}{error}{RESET}")
        return 1

    issues = validate_document(data)

    if issues:
        print(f"{RED}{[issue.message for issue in issues]}{RESET}")
        return 1

    print(f"{GREEN}success{RESET}")


    return 0


if __name__ == "__main__":
    raise SystemExit(main())