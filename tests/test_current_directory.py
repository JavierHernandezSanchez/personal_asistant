import pytest
from src.tools.current_directory import CurrentDirectoryTool
import os
from pathlib import Path

def test_returns_current_directory(tmp_path):
    # Change the current working directory to the temporary path
    original_cwd = Path.cwd()
    try:
        # Change to the temporary directory
        tmp_path.mkdir(exist_ok=True)
        os.chdir(tmp_path)

        # Execute the CurrentDirectoryTool
        tool = CurrentDirectoryTool()
        result = tool.execute([])

        # Assert that the result is the current working directory
        assert result == str(tmp_path)
    finally:
        # Change back to the original working directory
        os.chdir(original_cwd)

def test_raises_on_arguments():
    tool = CurrentDirectoryTool()
    with pytest.raises(ValueError) as excinfo:
        tool.execute(["unexpected_argument"])
    assert "No arguments are required." in str(excinfo.value)