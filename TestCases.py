
### Test Cases

#### test_file_system.py

import unittest
from FIlesystem.py import File, Directory, FileSystem

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()

    def test_create_file(self):
        self.fs.create_file("testfile.txt", "This is a test file.")
        file = self.fs.current_directory.get_file("testfile.txt")
        self.assertIsNotNone(file)
        self.assertEqual(file.name, "testfile.txt")
        self.assertEqual(file.content, "This is a test file.")

    def test_delete_file(self):
        self.fs.create_file("testfile.txt", "This is a test file.")
        self.fs.delete_file("testfile.txt")
        file = self.fs.current_directory.get_file("testfile.txt")
        self.assertIsNone(file)

    def test_create_directory(self):
        self.fs.create_directory("testdir")
        directory = self.fs.current_directory.get_directory("testdir")
        self.assertIsNotNone(directory)
        self.assertEqual(directory.name, "testdir")

    def test_delete_directory(self):
        self.fs.create_directory("testdir")
        self.fs.delete_directory("testdir")
        directory = self.fs.current_directory.get_directory("testdir")
        self.assertIsNone(directory)

    def test_change_directory(self):
        self.fs.create_directory("testdir")
        self.fs.change_directory("testdir")
        self.assertEqual(self.fs.current_directory.name, "testdir")
        self.fs.change_directory("..")
        self.assertEqual(self.fs.current_directory.name, "root")

    def test_list_contents(self):
        self.fs.create_directory("testdir")
        self.fs.create_file("testfile.txt", "This is a test file.")
        self.fs.list_contents()  # Manual verification in test output

if __name__ == '__main__':
    unittest.main()