import re
from datetime import datetime

def print_separator():
    print("\n----------------------------------\n")

# 1. Extract a numeric ID from text, first using a standard group, then using a named group.

# Standard Group
pattern_standard = re.compile(r"ID=(\d+)")
match_standard = pattern_standard.search("ID=482")

if match_standard is None:
    print("Standard Group: No match was found")
else:
    print(match_standard.group())

# Named Group
pattern_named = re.compile(r"ID=(?P<id>\d+)")
match_named = pattern_named.search("ID=482")

if match_named is None:
    print("Named Group: No match was found")
else:
    print(match_named.group("id"))


# 2. Extract the year, month, and day from 2026-08-15 and output the three groups separately.
print_separator()
def validate_date(match_pattern: re.Match) -> bool:
    try:
        print("Validating date ...")
        datetime.strptime(match_pattern.group("date"), "%Y-%m-%d")
        print(f"Year: {match_pattern.group("year")}")
        print(f"Month: {match_pattern.group("month")}")
        print(f"Day: {match_pattern.group("day")}")
        return True
    except ValueError as error:
        print(error)
        return False
    

log_example = "2026-02-28 10:21:31 INFO [api] Request started"
pattern_date = re.compile(r"(?P<date>(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}))")
match_date = pattern_date.match(log_example)

if match_date is None:
    print("Date: No match was found")
else:
    validate_date(match_date)


# 3. Use fullmatch() to check whether an input conforms entirely to the format ERROR [auth].
print_separator()
error_log = "2026-12-01 10:21:33 ERROR [auth] Invalid token"
pattern_error_log = re.compile(r"(?P<date>(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}))\s\d{2}:\d{2}:\d{2}\sERROR\s\[auth\]\s.+")
match_error_log = pattern_error_log.fullmatch(error_log)

if match_error_log is None:
    print("Error log: No match was found")
else:
    success = validate_date(match_error_log)
    if success:
        print(match_error_log.group())

