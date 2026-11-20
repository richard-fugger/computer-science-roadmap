from src.models import LogReport


def print_report(report: LogReport) -> None:
        print("------- Log Report -------")
        print(f"File Path: {report.path.resolve()}")
        print("--------------------------")
        print(f"Total lines: {report.total_lines}")
        print(f"Valid lines: {report.valid_lines}")
        print(f"Invalid lines: {report.total_lines - report.valid_lines}")
        print("--------------------------")
        if report.by_level:
            for level, count in report.by_level.items():
                print(f"{level}: {count}")
        else:
            print("No level entries.")
        print("--------------------------")
        if report.by_component:
            for component, count in report.by_component.items():
                print(f"{component}: {count}")
        else:
            print("No conponent entries.")
        print("--------------------------")
        if report.error_messages:
            message_list = report.error_messages.most_common(1)
            print(f"Most frequent error message: {message_list[0][0]} ({message_list[0][1]})")
        else:
            print("No error messages.")
        print("--------------------------")
        print(f"First error: {report.first_error}")
        print(f"Last error: {report.last_error}")