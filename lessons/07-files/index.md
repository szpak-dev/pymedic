# Lesson 7: Files

## Objectives

* Understand reading, writing, and appending to files in Python
* Learn about file modes and context management
* Use standard libraries for file operations
* Explore file locking, paths, and safety practices


## 1. Opening and Closing Files

### Syntax:

```python
file = open('example.txt', 'r')
data = file.read()
file.close()
```

### Best Practice — Using `with`:

```python
with open('example.txt', 'r') as file:
    data = file.read()
```

### Modes:

* `'r'`: read
* `'w'`: write (overwrite)
* `'a'`: append
* `'b'`: binary
* `'x'`: exclusive creation
* `'r+'`: read/write


## 2. Writing to Files

```python
with open('output.txt', 'w') as file:
    file.write("Hello, world!\n")
```

### Appending:

```python
with open('output.txt', 'a') as file:
    file.write("Additional line\n")
```


## 3. Reading Files

```python
with open('data.txt', 'r') as file:
    content = file.read()
```

### Reading Line by Line:

```python
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())
```


## 4. File Paths

### Using `os` and `pathlib`:

```python
from pathlib import Path
file_path = Path('data') / 'example.txt'
with file_path.open('r') as file:
    print(file.read())
```

### Absolute vs Relative Paths

* **Relative**: relative to current script or working directory
* **Absolute**: full path from root


## 5. Managing Files Without `with`

Using `with` is recommended, but you can manually open and close files too.

### Example:

```python
file = open('manual.txt', 'w')
try:
    file.write("Manual file management")
finally:
    file.close()
```

### Important:

* Always call `close()` or use `try-finally` to ensure resources are released
* Failure to close files may cause data loss or locking issues


## 6. Working with JSON Files

### Reading JSON:

```python
import json
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)
```

### Writing JSON:

```python
import json
patients = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]
with open('data.json', 'w') as file:
    json.dump(patients, file, indent=2)
```

### Updating JSON:

```python
with open('data.json', 'r+') as file:
    data = json.load(file)
    data.append({"id": 3, "name": "Charlie"})
    file.seek(0)
    json.dump(data, file, indent=2)
    file.truncate()
```

### Tips:

* Always use `seek(0)` and `truncate()` when updating JSON files in place
* Use `indent` for readable formatting
* Use `try-except` for safe parsing


## 7. Useful Libraries

* `os`: file existence, path operations
* `shutil`: file copying, moving, deleting
* `pathlib`: object-oriented file paths
* `tempfile`: temporary files
* `csv`, `json`: structured file formats


## 8. Safe File Handling Tips

* Always use `with` for automatic closure
* Validate file paths and handle exceptions
* Use `try-except` for IO errors
* Prefer `pathlib` for clarity and robustness

```python
from pathlib import Path
try:
    path = Path("config.json")
    with path.open('r') as f:
        config = f.read()
except FileNotFoundError:
    print("File not found")
```
