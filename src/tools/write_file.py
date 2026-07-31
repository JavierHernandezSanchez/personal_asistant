from src.tool import Tool
from pathlib import Path

class WriteFileTool(Tool):
    """
    Writes content to a specified file.

    This tool is responsible for creating a new file or overwriting an existing file with the provided content.
    If the file already exists, its previous contents are replaced.
    """    

    name = "write_file"
    description = "Writes content to a specified file."
    usage = "write_file <file_path> <content>"
    
    def execute(self, arguments: list[str]) -> str:
        if len(arguments) != 2:
            raise ValueError("Exactly two arguments (file_path and content) are required.")

        file_path = arguments[0]
        content = arguments[1]
        path = Path(file_path)

        if not path.parent.exists():
            raise FileNotFoundError(f"Directory '{path.parent}' does not exist.")

        path.write_text(content, encoding="utf-8")