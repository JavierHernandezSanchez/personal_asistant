import pytest
from src.tools.read_file import ReadFileTool

def test_reads_existing_file(tmp_path):
    # Create a temporary file with some content
    file_path = tmp_path / "test_file.txt"
    content = "Hello, World!"
    file_path.write_text(content)

    # Read the file using the function to be tested
    tool = ReadFileTool()
    result = tool.execute([str(file_path)])    

    # Assert that the content read from the file matches the expected content
    assert result == content

def test_reads_nonexistent_file(tmp_path):
    # Define a path to a non-existent file
    file_path = tmp_path / "nonexistent_file.txt"

    # Attempt to read the non-existent file 
    tool = ReadFileTool()
    with pytest.raises(FileNotFoundError):
        tool.execute([str(file_path)])

def test_reads_directory(tmp_path):
    # Create a temporary directory
    dir_path = tmp_path / "test_directory"
    dir_path.mkdir()

    # Attempt to read the directory 
    tool = ReadFileTool()
    with pytest.raises(IsADirectoryError):
        tool.execute([str(dir_path)])

def test_raises_on_no_arguments():
    # Attempt to read a file without providing any arguments
    tool = ReadFileTool()
    with pytest.raises(ValueError):
        tool.execute([])

def test_raises_on_multiple_arguments(tmp_path):
    # Create a temporary file with some content
    file_path = tmp_path / "test_file.txt"
    content = "Hello, World!"
    file_path.write_text(content)

    # Attempt to read a file with multiple arguments
    tool = ReadFileTool()
    with pytest.raises(ValueError):
        tool.execute([str(file_path), "extra_argument"])