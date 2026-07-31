import pytest
from src.tools.list_directory import ListDirectoryTool

def test_list_existing_directory(tmp_path):
    # Create a temporary directory with some files
    dir_path = tmp_path / "test_directory"
    dir_path.mkdir()
    (dir_path / "file1.txt").write_text("File 1 content")
    (dir_path / "file2.txt").write_text("File 2 content")

    # List the directory using the function to be tested
    tool = ListDirectoryTool()
    result = tool.execute([str(dir_path)])

    # Assert that the contents of the directory are listed correctly
    expected_contents = "file1.txt\nfile2.txt"
    assert result == expected_contents

def test_list_nonexistent_directory(tmp_path):
    # Define a path to a non-existent directory
    dir_path = tmp_path / "nonexistent_directory"

    # Attempt to list the non-existent directory
    tool = ListDirectoryTool()
    with pytest.raises(FileNotFoundError):
        tool.execute([str(dir_path)])

def test_list_file(tmp_path):
    # Create a temporary file
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("File content")

    # Attempt to list the contents of a file (should raise NotADirectoryError)
    tool = ListDirectoryTool()
    with pytest.raises(NotADirectoryError):
        tool.execute([str(file_path)])

def test_raises_on_no_arguments():
    # Attempt to list a directory without providing any arguments
    tool = ListDirectoryTool()
    with pytest.raises(ValueError):
        tool.execute([])

def test_raises_on_multiple_arguments(tmp_path):
    # Create a temporary directory
    dir_path = tmp_path / "test_directory"
    dir_path.mkdir()

    # Attempt to list a directory with multiple arguments
    tool = ListDirectoryTool()
    with pytest.raises(ValueError):
        tool.execute([str(dir_path), "extra_argument"])