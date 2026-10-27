# JSON Validator

## Purpose

A small command-line program that validates JSON files against a predefined structure and set of validation rules.

For each file, the program reports whether the document is valid. If validation issues occur, the corresponding issues are displayed.

## Requirements

- Python 3.12 or newer

## Installation

### Clone the reporitory:

```bash
git clone <repository-url>
cd <project-folder>
```

### Create a virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

### Install dependencies

```powershell
python -m pip install -r requirements.txt
```

To verify that pytest is installed:

```powershell
python -m pytest --version
```

### Run the program

```bash
python src/main.py <file_path>
```

## Example Valid JSON file

```json
{
    "items": [
        {
            "id": "item-001",
            "name": "Example",
            "value": 50,
            "enabled": true,
        }
    ]
}
```

The `enabled` field is optional.

## Validate Multiple JSON files

```powershell
phyton -m src.main input/valid.json input/invalid-ids.json
```

## Run Tests

Run the complete test suite:

```powershell
python -m pytest
```

## Project Structure Overview

```text
src/
├── main.py         -> CLI handling and program coordination
├── loader.py       -> loads and parses JSON files
├── validator.py    -> validates documents against the defined rules
├── output.py       -> formats and prints validation results
├── models.py       -> data models used by the application
├── constants.py    -> shared constants and validation codes
└── exceptions.py   -> custom application exceptions

tests/
├── test_loader.py       -> tests for JSON loading
├── test_validator.py    -> tests for validation rules
└── test_integration.py  -> integration tests

requirements.txt         -> project dependencies
```

