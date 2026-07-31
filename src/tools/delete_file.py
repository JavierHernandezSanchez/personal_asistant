from src.tool import Tool
import os
from pathlib import Path

class DeleteFileTool(Tool):
    name = "delete_file"
    description = "Deletes a specified file."
    usage = "delete_file <file_path>"

    def execute(self, arguments: list[str]) -> str:
        if len(arguments) != 1:
            raise ValueError("Exactly one argument (file_path) is required.")

        path = Path(arguments[0]).resolve()
        if not path.exists():
            raise FileNotFoundError(f"File '{path}' does not exist.")
        if not path.is_file():
            raise IsADirectoryError(f"'{path}' is not a file.")

        path.unlink()