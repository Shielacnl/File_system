class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content

    def __repr__(self):
        return f"File(name='{self.name}', content='{self.content}')"


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.directories = {}

    def __repr__(self):
        return f"Directory(name='{self.name}')"

    def add_file(self, file):
        self.files[file.name] = file

    def add_directory(self, directory):
        self.directories[directory.name] = directory

    def delete_file(self, filename):
        if filename in self.files:
            del self.files[filename]
        else:
            raise FileNotFoundError(f"File '{filename}' not found.")

    def delete_directory(self, dirname):
        if dirname in self.directories:
            del self.directories[dirname]
        else:
            raise FileNotFoundError(f"Directory '{dirname}' not found.")

    def get_file(self, filename):
        return self.files.get(filename, None)

    def get_directory(self, dirname):
        return self.directories.get(dirname, None)


class FileSystem:
    def __init__(self):
        self.root = Directory("root")
        self.current_directory = self.root
        self.path = ["root"]

    def create_file(self, filename, content=""):
        new_file = File(filename, content)
        self.current_directory.add_file(new_file)

    def delete_file(self, filename):
        self.current_directory.delete_file(filename)

    def create_directory(self, dirname):
        new_directory = Directory(dirname)
        self.current_directory.add_directory(new_directory)

    def delete_directory(self, dirname):
        self.current_directory.delete_directory(dirname)

    def change_directory(self, dirname):
        if dirname == "..":
            if len(self.path) > 1:
                self.path.pop()
                self.current_directory = self.root
                for dir in self.path[1:]:
                    self.current_directory = self.current_directory.get_directory(dir)
        else:
            new_directory = self.current_directory.get_directory(dirname)
            if new_directory:
                self.current_directory = new_directory
                self.path.append(dirname)
            else:
                raise FileNotFoundError(f"Directory '{dirname}' not found.")

    def list_contents(self):
        print(f"Path: {'/'.join(self.path)}")
        print("Directories:")
        for dirname in self.current_directory.directories:
            print(dirname)
        print("Files:")
        for filename in self.current_directory.files:
            print(filename)
