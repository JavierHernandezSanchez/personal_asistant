import pytest
from src.tools.write_file import WriteFileTool

def test_create_and_write_file(tmp_path):
    # Define a file path and content
    file_path = tmp_path / "test_file.txt"
    content = "This is a test."

    # Write to the file using the function to be tested
    tool = WriteFileTool()
    tool.execute([str(file_path), content])

    # Assert that the file was created and contains the expected content
    assert file_path.exists()
    assert file_path.read_text() == content

def test_overwrite_existing_file(tmp_path):
    # Create a temporary file with initial content
    file_path = tmp_path / "test_file.txt"
    initial_content = "Initial content."
    file_path.write_text(initial_content)

    # Define new content to overwrite the existing file
    new_content = "New content."

    # Write to the file using the function to be tested
    tool = WriteFileTool()
    tool.execute([str(file_path), new_content])

    # Assert that the file's content was overwritten with the new content
    assert file_path.read_text() == new_content

def test_write_to_nonexistent_directory(tmp_path):
    # Define a file path in a non-existent directory
    dir_path = tmp_path / "nonexistent_directory"
    file_path = dir_path / "test_file.txt"
    content = "This is a test."

    # Attempt to write to the file using the function to be tested
    tool = WriteFileTool()
    with pytest.raises(FileNotFoundError):
        tool.execute([str(file_path), content])

def test_write_to_directory_instead_of_file(tmp_path):
    # Create a temporary directory
    dir_path = tmp_path / "test_directory"
    dir_path.mkdir()

    # Attempt to write to the directory using the function to be tested
    tool = WriteFileTool()
    with pytest.raises(IsADirectoryError):
        tool.execute([str(dir_path), "This should fail."])

def test_raises_on_no_arguments():
    # Attempt to write to a file without providing any arguments
    tool = WriteFileTool()
    with pytest.raises(ValueError):
        tool.execute([])

def test_raises_on_no_content(tmp_path):
    # Create a temporary file path
    file_path = tmp_path / "test_file.txt"

    # Attempt to write to a file without providing content
    tool = WriteFileTool()
    with pytest.raises(ValueError):
        tool.execute([str(file_path)])