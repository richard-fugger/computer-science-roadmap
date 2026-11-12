import argparse
from pathlib import Path

from src.constants import RED, RESET
from src.exceptions import JsonValidatorError
from src.loader import load_json
from src.models import FileValidationResult
from src.output import print_validation_results
from src.validator import validate_document


def parse_args(argv: list[str] | None = None):
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    had_error = False
    has_issues = False
    item_printed = False

    for file in args.files:
        try:
        
            json_content = load_json(Path(file))
            issues = validate_document(json_content)
            if issues:
                has_issues = True
            validation_result = FileValidationResult(
                file_path = Path(file),
                issues = issues
            )
            print_validation_results(validation_result, item_printed)
            item_printed = True

        except JsonValidatorError as error:
            print(f"{RED}{error}{RESET}")
            had_error = True

    if had_error or has_issues:
        return 1

    return 0



if __name__ == "__main__":
    raise SystemExit(main())