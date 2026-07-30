import pytest
from src.tools.read_file import ReadFileTool

def test_read_existing_file(tmp_path):
    # Create a temporary file with some content
    file_path = tmp_path / "test_file.txt"
    content = "Hello, World!"
    file_path.write_text(content)

    # Read the file using the function to be tested
    tool = ReadFileTool()
    result = tool.execute(file_path)    

    # Assert that the content read from the file matches the expected content
    assert result == content

def test_read_nonexistent_file(tmp_path):
    # Define a path to a non-existent file
    file_path = tmp_path / "nonexistent_file.txt"

    # Attempt to read the non-existent file 
    tool = ReadFileTool()
    with pytest.raises(FileNotFoundError):
        tool.execute(file_path)

def test_read_directory(tmp_path):
    # Create a temporary directory
    dir_path = tmp_path / "test_directory"
    dir_path.mkdir()

    # Attempt to read the directory 
    tool = ReadFileTool()
    with pytest.raises(IsADirectoryError):
        tool.execute(dir_path)