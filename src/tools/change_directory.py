from src.tool import Tool
from pathlib import Path
import os

class ChangeDirectoryTool(Tool):
    """
    Changes the current working directory to the specified path.

    This tool allows the assistant to change its working directory, enabling it to operate in different
    parts of the filesystem. It does not return any output but will raise an error if the specified
    path is invalid or inaccessible.
    """
    name = "change_directory"
    description = "Changes the current working directory to the specified path."
    usage = "change_directory <path>"
    
    def execute(self, arguments: list[str]) -> None:
        if len(arguments) != 1:
            raise ValueError("Exactly one argument (the target directory) is required.")
        
        path = Path(arguments[0])

        if not path.exists():
            raise FileNotFoundError(f"The specified path does not exist: {path}")
        
        if not path.is_dir():
            raise NotADirectoryError(f"The specified path is not a directory: {path}")

        os.chdir(path)