# File System Simulation

This project simulates a simple file system with basic functionalities including file creation, deletion, and directory management.

## Features
- Create files and directories
- Delete files and directories
- Change the current working directory
- List contents of the current directory

## Classes
### File
Represents a file with a name and content.

**Attributes:**
- `name`: The name of the file.
- `content`: The content of the file.

**Methods:**
- `__init__(self, name, content="")`: Initializes a new file.
- `__repr__(self)`: Returns a string representation of the file.

### Directory
Represents a directory containing files and other directories.

**Attributes:**
- `name`: The name of the directory.
- `files`: A dictionary of files in the directory.
- `directories`: A dictionary of directories in the directory.

**Methods:**
- `__init__(self, name)`: Initializes a new directory.
- `__repr__(self)`: Returns a string representation of the directory.
- `add_file(self, file)`: Adds a file to the directory.
- `add_directory(self, directory)`: Adds a sub-directory to the directory.
- `delete_file(self, filename)`: Deletes a file from the directory.
- `delete_directory(self, dirname)`: Deletes a sub-directory from the directory.
- `get_file(self, filename)`: Retrieves a file from the directory.
- `get_directory(self, dirname)`: Retrieves a sub-directory from the directory.

### FileSystem
Manages the overall file system with a root directory and the current working directory.

**Attributes:**
- `root`: The root directory of the file system.
- `current_directory`: The current working directory.
- `path`: The path of the current working directory.

**Methods:**
- `__init__(self)`: Initializes a new file system.
- `create_file(self, filename, content="")`: Creates a new file in the current directory.
- `delete_file(self, filename)`: Deletes a file from the current directory.
- `create_directory(self, dirname)`: Creates a new directory in the current directory.
- `delete_directory(self, dirname)`: Deletes a directory from the current directory.
- `change_directory(self, dirname)`: Changes the current working directory.
- `list_contents(self)`: Lists the contents of the current directory.

## Usage
Below is an example of how to use the File System:

```python
fs = FileSystem()
fs.create_directory("docs")
fs.change_directory("docs")
fs.create_file("file1.txt", "Hello, World!")
fs.create_file("file2.txt", "Another file")
fs.list_contents()
fs.change_directory("..")
fs.list_contents()
