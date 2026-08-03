# Environment, Terminal, and First File Analysis

**Start:** 22:00

---

## Block 1: Project Setup

### GitHub and Git Setup

To check which GitHub accounts are authenticated with the GitHub CLI and which account is currently active, use:

```powershell
gh auth status
```

To switch between GitHub accounts already authenticated with the GitHub CLI, use:

```powershell
gh auth switch --user "username"
```

To clone an existing GitHub repository, run the following command from the directory in which the repository folder should be created:

```powershell
git clone https://github.com/username/repository-name.git
```

`git clone` creates a new local repository directory, checks out the repository files, creates the hidden `.git` directory, and usually configures the source repository as the remote named `origin`.

After cloning the repository, enter the new repository directory:

```powershell
cd repository-name
```

To configure the author name stored in future commits for the current repository, use:

```powershell
git config user.name "Your Name"
```

Adding the `--global` option would apply the configuration to all repositories on the device instead:

```powershell
git config --global user.name "Your Name"
```

Once you are inside the repository directory, configure the email address stored in future commits with:

```powershell
git config user.email "your-email@example.com"
```

GitHub can associate commits with your account when the configured email address is connected to that GitHub account.

To configure the email address globally for all repositories, use:

```powershell
git config --global user.email "your-email@example.com"
```

The Git author name and email are configured separately from the GitHub account authenticated with the GitHub CLI. However, the commit email should be connected to the correct GitHub account so that GitHub can attribute the commits to that account.



### Project Structure
To create and navigate the project structure from the terminal, the following PowerShell commands are useful:
* `Get-Location` (`pwd`): Displays the current working directory.
* `Set-Location` (`cd`): Changes the current working directory. Use `cd ..` to move to the parent directory.
* `Get-ChildItem` (`gci`): Displays the files and directories inside the current working directory. With `Get-ChildItem "path"` you can display the contents of any directory independently of the current working directory.
* `New-Item -ItemType Directory -Path "directory-name"`: Creates a new directory at the specified path.
* `mkdir "directory-name"`: Shorter command for creating a directory.
* `New-Item -ItemType File -Path "file-name"`: Creates a new file at the specified destination

### Key Concepts
* Working directory: The working directory is the directory in which the terminal is currently opreating. Relative paths are interpreted starting from this directory.
* Absolute path: An absolute path specifies the complete location starting from the drive root.
* Relative path: A relative path specifies a location starting from the current working directory.
* Switching directories: To change the current working directory, use `cd "path"`.

---

## Block 2: Python Virtual Environment
A virtual environment isolates the Python packages installed for a project from the global Python installation and from other projects.
Using a separate virtual environment for each project allows different projects to use different package versions without conflicts.

To create a virtual environment `named .venv`, run the following command from the project directory:

```powershell 
python -m venv .venv
```

The virtual environment should normally be activated whenever a new terminal session is opened for the project.

To activate the virtual environment in PowerShell, use:

```powershell
.\.venv\Scripts\Activate.ps1
```

To display the version of the Python interpreter currently selected by the python command, use:

```powershell
python --version
```

Python source files use the `.py` file extension.
You can execute the file from the terminal, for example: `python src/main.py`.

---

## First Python Exercise (Block 3)
### Task: File and Folder Analyzer

Write a program that:

1. Stores a folder path in a variable.
2. Finds all direct contents of that folder.
3. Outputs only files.
4. Displays the name and size of each file.

Use `pathlib` wherever possible.

#### Example Output

```text
README.md - 1.2 KB
main.py - 430 Bytes
data.json - 2.8 KB
```


### Python pathlib – Basic Methods

| Methode oder Eigenschaft | Bedeutung                           |
| ------------------------ | ----------------------------------- |
| `Path.cwd()`             | Aktuelles Arbeitsverzeichnis        |
| `Path.home()`            | Benutzerverzeichnis                 |
| `path.name`              | Datei- oder Ordnername              |
| `path.parent`            | Übergeordnetes Verzeichnis          |
| `path.exists()`          | Prüft, ob der Pfad existiert        |
| `path.is_file()`         | Prüft, ob der Pfad eine Datei ist   |
| `path.is_dir()`          | Prüft, ob der Pfad ein Ordner ist   |
| `path.iterdir()`         | Gibt direkte Ordnerinhalte zurück   |
| `path.glob("pattern")`   | Sucht nach einem Muster             |
| `path.stat().st_size`    | Gibt die Dateigröße in Bytes zurück |
| `path.mkdir()`           | Erstellt einen Ordner               |
| `path.touch()`           | Erstellt eine leere Datei           |
| `path.read_text()`       | Liest eine Textdatei                |
| `path.write_text()`      | Schreibt eine Textdatei             |
| `path.unlink()`          | Löscht eine Datei                   |

---

## Git (Block 4)

To create and switch to a new branch, use:

```powershell
git switch -c phase-01-week-01
```

To stage all current changes, use:

```powershell
git add .
```

To commit the staged changes, use:

```powershell
git commit -m "Set up week 1 file analyzer"
```

When pushing the new branch to the remote repository for the first time, use:

```powershell
git push -u origin phase-01-week-01
```

The `-u` option connects the local branch to the corresponding remote branch. After this upstream connection has been created, future commits can normally be pushed with:

```powershell
git push
```

**End** 00:30