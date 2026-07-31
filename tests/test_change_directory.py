import pytest
from src.tools.change_directory import ChangeDirectoryTool
from pathlib import Path
import os

def test_changes_current_directory(tmp_path):
    # Create a temporary directory to change into
    target_dir = tmp_path / "target"
    target_dir.mkdir()

    # Store the original current working directory
    original_cwd = Path.cwd()

    try:
        # Execute the ChangeDirectoryTool
        tool = ChangeDirectoryTool()
        tool.execute([str(target_dir)])

        # Assert that the current working directory has changed
        assert Path.cwd() == target_dir
    finally:
        # Change back to the original working directory
        os.chdir(original_cwd)

def test_raises_on_no_arguments():
    tool = ChangeDirectoryTool()
    with pytest.raises(ValueError) as excinfo:
        tool.execute([])
    assert "Exactly one argument (the target directory) is required." in str(excinfo.value)

def test_raises_on_multiple_arguments():
    tool = ChangeDirectoryTool()
    with pytest.raises(ValueError) as excinfo:
        tool.execute(["arg1", "arg2"])
    assert "Exactly one argument (the target directory) is required." in str(excinfo.value)

def test_raises_directory_not_found():
    tool = ChangeDirectoryTool()
    with pytest.raises(FileNotFoundError) as excinfo:
        tool.execute(["/non/existent/directory"])
    assert "The specified path does not exist:" in str(excinfo.value)

def test_raises_not_a_directory():
    tool = ChangeDirectoryTool()
    with pytest.raises(NotADirectoryError) as excinfo:
        tool.execute(["/etc/passwd"])  # This is a file, not a directory
    assert "The specified path is not a directory:" in str(excinfo.value)