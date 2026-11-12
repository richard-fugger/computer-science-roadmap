from src.constants import GREEN, RED, RESET
from src.models import FileValidationResult


def print_validation_results(validation_results: FileValidationResult, print_space_bar: bool):
    if print_space_bar:
        print()

    print(f"File: {validation_results.file_path.name}:")

    if validation_results.is_valid():
        print(f"{GREEN}{validation_results.file_path.name} is valid.{RESET}")
        return
    
    for issue in validation_results.issues:
        print(f"{issue.path}: {RED}{issue.message}{RESET}")