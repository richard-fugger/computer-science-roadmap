import argparse
from pathlib import Path

from src.constants import RED, RESET
from src.exceptions import JsonValidatorError
from src.loader import load_json
from src.models import FileValidationResult
from src.output import print_validation_results
from src.validator import validate_document


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()

    item_printed = False
    try:
        for file in args.files:
            json_content = load_json(Path(file))
            issues = validate_document(json_content)
            validation_result = FileValidationResult(
                file_path = Path(file),
                issues = issues
            )
            print_validation_results(validation_result, item_printed)
            item_printed = True

    except JsonValidatorError as error:
        print(f"{RED}{error}{RESET}")
        return



if __name__ == "__main__":
    main()