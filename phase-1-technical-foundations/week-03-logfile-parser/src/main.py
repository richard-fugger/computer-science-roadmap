from collections import Counter
from datetime import datetime
from pathlib import Path

from src.models import LogReport
from src.pipeline import iter_parsed_lines
from src.reporting import print_report


def main():
    FILE_PATH = Path("samples/small.log")

    report = LogReport(
        path = FILE_PATH,
        total_lines = 0,
        valid_lines = 0,
        by_level = Counter(),
        by_component = Counter(),
        error_messages = Counter(),
        first_error = datetime.max,
        last_error = datetime.min
    )

    try:
        for line_number, parsed_line in iter_parsed_lines(FILE_PATH):
            report.update_report(parsed_line)

    except FileNotFoundError as error:
        print(error)
        return
    except PermissionError as error:
        print(error)
        return
    except OSError as error:
        print(error)
        return

    else:
        print_report(report)


if __name__ == "__main__":
    main()