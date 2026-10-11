# Directory Analyzer

## Purpose

A small program that analyzes your specified directory and providex information such as:

* Number of files
* Number of directories
* Total size of all files
* Largest files (nuber can be specified)
* File-extensions and their number

## Requirement

* Python 3.12 or newer

## Installation

### Clone the reporitory:

```bash
git clone <repository-url>
cd <project-folder>
```

### Create a virtual environment:

Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Windows Command Prompt

```bash
.venv\Scripts\activate.bat
```

macOS / Linux

```bash
source .venv/bin/activate
```

### Run the program

```bash
python src/main.py <directory>
```

## CLI Examples

### Analyze a directory

```bash
python src/main.py D:/example
```

### Export analysis in a JSON file

```bash
python src/main.py D:/example --json
```

### Specify the json output-path

```bash
python src/main.py D:/example --json --output D:/analysis/report.json
```

### Specify limit of largest files (deault=5)

```bash
python src/main.py D:/example --top 3
```

