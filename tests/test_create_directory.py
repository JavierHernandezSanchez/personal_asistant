import pytest
from src.tools.create_directory import CreateDirectoryTool
from pathlib import Path

def test_creates_directory(tmp_path):
    # Create a temporary directory to serve as the parent
    parent_dir = tmp_path / "parent"
    parent_dir.mkdir()

    # Define the new directory name
    new_dir_name = "new_directory"
    new_dir_path = parent_dir / new_dir_name

    # Execute the CreateDirectoryTool
    tool = CreateDirectoryTool()
    tool.execute([str(new_dir_path)])

    # Assert that the new directory has been created
    assert new_dir_path.exists() and new_dir_path.is_dir()

def test_raises_on_no_arguments():
    tool = CreateDirectoryTool()
    with pytest.raises(ValueError) as excinfo:
        tool.execute([])
    assert "Exactly one argument (directory_path) is required." in str(excinfo.value)

def test_raises_on_multiple_arguments():
    tool = CreateDirectoryTool()
    with pytest.raises(ValueError) as excinfo:
        tool.execute(["arg1", "arg2"])
    assert "Exactly one argument (directory_path) is required." in str(excinfo.value)

def test_raises_parent_not_found():
    tool = CreateDirectoryTool()
    with pytest.raises(FileNotFoundError) as excinfo:
        tool.execute(["/non/existent/directory/new_directory"])    

def test_raises_directory_exists():
    # Create a temporary directory
    tmp_dir = Path("/tmp/test_directory")
    tmp_dir.mkdir(exist_ok=True)

    tool = CreateDirectoryTool()
    with pytest.raises(FileExistsError) as excinfo:
        tool.execute([str(tmp_dir)])
    assert "The specified path already exists:" in str(excinfo.value)