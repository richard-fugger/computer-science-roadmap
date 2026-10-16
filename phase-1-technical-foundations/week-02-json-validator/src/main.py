import argparse

from src.loader import load_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    args = parser.parse_args()

    obj = load_json(args.filepath)
    print(type(obj))


if __name__ == "__main__":
    main()