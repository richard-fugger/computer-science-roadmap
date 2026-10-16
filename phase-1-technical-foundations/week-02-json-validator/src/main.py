import argparse
from pathlib import Path

from src.loader import load_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    args = parser.parse_args()

    obj = load_json(Path(args.filepath))
    print(type(obj))


if __name__ == "__main__":
    main()