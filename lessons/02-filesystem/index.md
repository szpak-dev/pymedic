# Lesson 2: Introduction to Filesystem, Running Scripts and Basic Syntax

Welcome to your second lesson in Python. In this session, you'll:

- Learn about filesystem and basic files management using console
- Understand Python's internal file organization across different Operating Systems
- Learn how to run Python scripts
- Explore popular IDEs like VSCode and Jupyter Notebook
- Get familiar with Python’s basic syntax
- Complete a homework assignment that reinforces these concepts

## What is a Filesystem?

A filesystem is a method used by operating systems to store and organize files on a storage device, such as a hard drive or SSD. It determines how data is stored, retrieved, and managed.

### Key Differences on Linux, Mac, and Windows

| Feature | Linux | Mac | Windows |
|---------|-------|-----|---------|
| **Primary Filesystems** | ext4, Btrfs, XFS | APFS, HFS+ | NTFS, FAT32, exFAT |
| **Case Sensitivity** | Case-sensitive | Case-insensitive (by default) | Case-insensitive |
| **File Naming** | Almost any character, including / | Almost any character, including : | Restricted characters: \ / : * ? " < > | |
| **Permissions** | Uses read, write, execute permissions for user, group, and others | Uses Unix-like permissions | Uses ACLs (Access Control Lists) |
| **Path Separator** | / | / | \ |

### Differences Between Text and Binary Files

| Feature | Text Files | Binary Files |
|---------|------------|--------------|
| **Content** | Human-readable characters | Non-human-readable data |
| **Editing** | Can be edited with text editors | Require specialized software |
| **Examples** | .txt, .csv, .html | .exe, .jpg, .png |
| **Encoding** | Uses character encodings like ASCII or UTF-8 | Contains raw binary data |

### What Are Folders, Internally?

Folders, also known as directories, are a way to organize files on a filesystem. Internally, a folder is a special type of file that contains a list of entries. Each entry represents either a file or another folder. These entries include metadata such as the name, size, and location of the file or folder on the storage device.

### Basic Commands for Managing Files and Folders

#### Linux and Mac (Terminal)

| Command | Description |
|---------|-------------|
| `ls` | List files and folders |
| `cd <directory>` | Change directory |
| `pwd` | Print working directory |
| `mkdir <directory>` | Create a new directory |
| `rmdir <directory>` | Remove an empty directory |
| `rm <file>` | Remove a file |
| `cp <source> <destination>` | Copy a file |
| `mv <source> <destination>` | Move or rename a file |
| `touch <file>` | Create a new empty file |
| `cat <file>` | Display the contents of a file |
| `nano <file>` or `vi <file>` | Edit a file using a text editor |

#### Windows (Command Prompt)

| Command | Description |
|---------|-------------|
| `dir` | List files and folders |
| `cd <directory>` | Change directory |
| `cd` | Print working directory |
| `mkdir <directory>` | Create a new directory |
| `rmdir <directory>` | Remove an empty directory |
| `del <file>` | Delete a file |
| `copy <source> <destination>` | Copy a file |
| `move <source> <destination>` | Move or rename a file |
| `type nul > <file>` | Create a new empty file |
| `type <file>` | Display the contents of a file |
| `notepad <file>` | Edit a file using Notepad |


### Python File and Folder Structure

#### macOS

Python is typically installed in:

```
/opt/homebrew/Cellar/python@<version>/
```

User scripts and packages go into:

```
~/Library/Python/<version>/
```

#### Linux

Python is located in:

```
/usr/bin/python3
/usr/lib/python3.<version>/
```

User site-packages:

```
~/.local/lib/python3.<version>/
```

#### Windows

Installed in:

```
C:\Users\<Username>\AppData\Local\Programs\Python\Python<version>\
```

Scripts and site-packages:

```
C:\Users\<Username>\AppData\Roaming\Python\Python<version>\
```

## Running Python Scripts

You can run your Python script in two ways.

### Direct Execution

```shell
python script.py
```

- Runs the script `script.py` directly.
- Python looks for `script.py` in the current directory or the path specified
- If `script.py `imports other modules, Python will look for those modules in the PYTHONPATH or the standard library paths
- This is the most common way to run a Python script

### Module Execution

```shell
python -m script
```

- This command runs the module script as the main module
- Python looks for the module script in the `PYTHONPATH` or the standard library paths. It does not look for a file named script in the current directory unless the current directory is in the `PYTHONPATH`
- Useful when you want to run a module that is part of a package. It ensures that the module is run within the context of the package, which can be important for relative imports
- This is particularly useful for running modules that are part of a larger package or for testing modules

### Environment Variables and PYTHONPATH

Environment variables are dynamic values that can affect the behavior of processes and applications on a computer. They are part of the environment in which a process runs and can be used to store information such as paths to executable files, configuration settings, and other system-wide or user-specific data.

#### PYTHONPATH

`PYTHONPATH` is a specific environment variable that plays a crucial role in Python programming. It is used to specify additional directories where Python should look for modules and packages. When you import a module in Python, the interpreter searches for the module in the following locations:

1. The directory containing the input script (or the current directory if running interactively).
2. The directories listed in the `PYTHONPATH` environment variable.
3. The installation-dependent default directories, which typically include the standard library and site-packages directories.

#### Setting PYTHONPATH

You can set the `PYTHONPATH` environment variable to include additional directories where your Python modules are located. This can be done in several ways, depending on your operating system:

- **Linux and Mac**: You can set the `PYTHONPATH` in the terminal using the `export` command. For example:
  ```sh
  export PYTHONPATH="/path/to/your/module:$PYTHONPATH"
  ```

  To make this change permanent, you can add the `export` command to your shell configuration file, such as `.bashrc` or `.zshrc`.

- **Windows**: You can set the `PYTHONPATH` using the `set` command in the Command Prompt:
  ```cmd
  set PYTHONPATH=C:\path\to\your\module;%PYTHONPATH%
  ```

  To make this change permanent, you can add the `set` command to your system environment variables through the System Properties dialog.

#### Example

Suppose you have a custom Python module located in `/path/to/your/module`. To ensure that Python can find and import this module, you can set the `PYTHONPATH` as follows:

- **Linux and Mac**:
  ```sh
  export PYTHONPATH="/path/to/your/module:$PYTHONPATH"
  ```

- **Windows**:
  ```cmd
  set PYTHONPATH=C:\path\to\your\module;%PYTHONPATH%
  ```

After setting the `PYTHONPATH`, you can import modules from the specified directory in your Python scripts without needing to use relative or absolute paths.

#### Importance of PYTHONPATH

Setting the `PYTHONPATH` correctly is essential for managing dependencies and ensuring that your Python scripts can locate and import the necessary modules. It is particularly useful in larger projects where modules are organized into packages and sub-packages, and you need to ensure that all parts of the project can access the required modules.


## IDE Overview

### VSCode

- Lightweight, fast, and supports extensions
- Integrated terminal for running scripts
- [IntelliSense](https://code.visualstudio.com/docs/editing/intellisense) and [linting](https://en.wikipedia.org/wiki/Lint_(software)) support

### Jupyter Notebook

- Ideal for data analysis and prototyping
- Run cells interactively

Install and run:

```bash
pip install notebook
jupyter notebook
```

## Basic Syntax

### Variables and Types

```python
name: str = "Alice"
age: int = 30
height: float = 5.6
```

### Functions

```python
def greet(user: str) -> str:
    return f"Hello, {user}"
```

### Control Flow

```python
def is_adult(age: int) -> bool:
    if age >= 18:
        return True
    return False
```

### Lists and Loops

```python
users: list[str] = ["Alice", "Bob", "Charlie"]

for user in users:
    print(greet(user))
```

### Dictionaries

```python
person: dict[str, int] = {"Alice": 30, "Bob": 25}
```

## Homework

#### Objective
The objective of this assignment is to familiarize yourself with basic filesystem operations, including navigating directories, creating, moving, copying, and deleting files and folders. You will perform these operations using the command line interface (CLI) on your operating system.

#### Tasks

1. **Navigate the Filesystem**
   - Open your terminal (Linux/Mac) or Command Prompt (Windows).
   - Use the `cd` command to navigate to your home directory.
   - List the contents of the home directory using the `ls` (Linux/Mac) or `dir` (Windows) command.

2. **Create Directories**
   - Create a new directory called `my_filesystem` in your home directory.
   - Navigate into the `my_filesystem` directory.
   - Inside `my_filesystem`, create the following directories: `Documents`, `Images`, `Music`, and `Videos`.

3. **Create Files**
   - Navigate into the `Documents` directory.
   - Create three empty text files named `file1.txt`, `file2.txt`, and `file3.txt`.
   - Use a text editor to add some text to each of these files.

4. **Copy Files**
   - Copy `file1.txt` from the `Documents` directory to the `Images` directory.
   - Copy `file2.txt` from the `Documents` directory to the `Music` directory.
   - Copy `file3.txt` from the `Documents` directory to the `Videos` directory.

5. **Move Files**
   - Move `file1.txt` from the `Images` directory to the `Music` directory.
   - Move `file2.txt` from the `Music` directory to the `Videos` directory.
   - Move `file3.txt` from the `Videos` directory to the `Images` directory.

6. **Rename Files**
   - Rename `file1.txt` in the `Music` directory to `renamed_file1.txt`.
   - Rename `file2.txt` in the `Videos` directory to `renamed_file2.txt`.
   - Rename `file3.txt` in the `Images` directory to `renamed_file3.txt`.

7. **Delete Files and Directories**
   - Delete `renamed_file1.txt` from the `Music` directory.
   - Delete `renamed_file2.txt` from the `Videos` directory.
   - Delete the `Images` directory along with its contents.

8. **Search for Files**
   - Use the `find` command (Linux/Mac) or `dir /s` command (Windows) to search for `renamed_file3.txt` in the `my_filesystem` directory.
   - Note the path where the file is located.

9. **Generate a Directory Tree**
   - Use the `tree` command (Linux/Mac/Windows) to generate a visual representation of the `my_filesystem` directory structure.
   - If the `tree` command is not available, install it or use an alternative method to display the directory structure.

#### Example Commands

Here are some example commands to help you get started:

- **Navigate to home directory**:
  ```sh
  cd ~
  ```

- **List contents of the current directory (Linux/Mac)**:
  ```sh
  ls
  ```

- **List contents of the current directory (Windows)**:
  ```cmd
  dir
  ```

- **Create a new directory**:
  ```sh
  mkdir my_filesystem
  ```

- **Navigate into a directory**:
  ```sh
  cd my_filesystem
  ```

- **Create an empty file (Linux/Mac)**:
  ```sh
  touch file1.txt
  ```

- **Create an empty file (Windows)**:
  ```cmd
  type nul > file1.txt
  ```

- **Copy a file (Linux/Mac)**:
  ```sh
  cp file1.txt ../Images/
  ```

- **Copy a file (Windows)**:
  ```cmd
  copy file1.txt ..\Images\
  ```

- **Move a file (Linux/Mac)**:
  ```sh
  mv file1.txt ../Music/
  ```

- **Move a file (Windows)**:
  ```cmd
  move file1.txt ..\Music\
  ```

- **Rename a file (Linux/Mac)**:
  ```sh
  mv file1.txt renamed_file1.txt
  ```

- **Rename a file (Windows)**:
  ```cmd
  ren file1.txt renamed_file1.txt
  ```

- **Delete a file (Linux/Mac)**:
  ```sh
  rm renamed_file1.txt
  ```

- **Delete a file (Windows)**:
  ```cmd
  del renamed_file1.txt
  ```

- **Delete a directory and its contents (Linux/Mac)**:
  ```sh
  rm -rf Images
  ```

- **Delete a directory and its contents (Windows)**:
  ```cmd
  rmdir /s /q Images
  ```

- **Search for a file (Linux/Mac)**:
  ```sh
  find . -name "renamed_file3.txt"
  ```

- **Search for a file (Windows)**:
  ```cmd
  dir /s renamed_file3.txt
  ```

- **Generate a directory tree (Linux/Mac)**:
  ```sh
  tree
  ```

- **Generate a directory tree (Windows)**:
  ```cmd
  tree
  ```

#### Submission

Submit a text file containing the following:

1. A list of all the commands you used to complete the tasks.
2. Screenshots or terminal output showing the results of each task.
3. A brief explanation of any challenges you faced and how you overcame them.

Good luck!