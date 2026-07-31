from src.tool import Tool
from pathlib import Path

class CreateDirectoryTool(Tool):
    """
    Tool to create a single directory.

    This tool allows the assistant to create a new directory at the specified path.
    """
    name = "create_directory"
    usage = "create_directory <directory_path>"

    def execute(self, arguments: list[str]) -> None:
        if len(arguments) != 1:
            raise ValueError("Exactly one argument (directory_path) is required.")

        path = Path(arguments[0])

        if path.exists():
            raise FileExistsError(f"The specified path already exists: {path}")
        
        path.mkdir()        