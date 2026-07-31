import pytest
from src.tools.delete_file import DeleteFileTool

def test_deletes_existing_file(tmp_path):
    # Create a temporary file to delete
    temp_file = tmp_path / "temp_file.txt"
    temp_file.write_text("Temporary file content")

    # Ensure the file exists before deletion
    assert temp_file.exists()

    # Execute the DeleteFileTool    
    tool = DeleteFileTool()
    tool.execute([str(temp_file)])

    # Assert that the file has been deleted
    assert not temp_file.exists()

def test_deletes_empty_file(tmp_path):
    # Create an empty temporary file to delete
    empty_file = tmp_path / "empty_file.txt"
    empty_file.touch()  # Create an empty file

    # Ensure the file exists before deletion
    assert empty_file.exists()

    # Execute the DeleteFileTool    
    tool = DeleteFileTool()
    tool.execute([str(empty_file)])

    # Assert that the file has been deleted
    assert not empty_file.exists()

def test_raises_on_no_arguments():
    tool = DeleteFileTool()
    with pytest.raises(ValueError) as excinfo:
        tool.execute([])
    assert "Exactly one argument (file_path) is required." in str(excinfo.value)

def test_raises_on_multiple_arguments():
    tool = DeleteFileTool()
    with pytest.raises(ValueError) as excinfo:
        tool.execute(["arg1", "arg2"])
    assert "Exactly one argument (file_path) is required." in str(excinfo.value)

def test_raises_file_not_found():
    tool = DeleteFileTool()
    with pytest.raises(FileNotFoundError) as excinfo:
        tool.execute(["/non/existent/file.txt"])
    assert "File '/non/existent/file.txt' does not exist." in str(excinfo.value)

def test_raises_is_a_directory(tmp_path):
    directory = tmp_path / "my_directory"
    directory.mkdir()
    tool = DeleteFileTool()
    with pytest.raises(IsADirectoryError) as excinfo:
        tool.execute([str(directory)])
    assert f"'{directory}' is not a file." in str(excinfo.value)