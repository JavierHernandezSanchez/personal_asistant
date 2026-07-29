from tool import Tool
from pathlib import Path

class ReadFileTool(Tool):
    """
    Reads the content of a specified file.

    This tool is responsible for opening a text file and returning its content as a string.

    It does not parse, summarize, validate or modify the file.
    """

    name = "read_file"
    description = "Reads the content of a specified file."
    usage = "read_file <file_path>"
    
    def execute(self, file_path: str) -> str:
        path = Path(file_path)

        if not path.exists():            
            raise FileNotFoundError(f"File '{file_path}' does not exist.")
        
        if not path.is_file():
            raise IsADirectoryError(f"'{file_path}' is not a file.")        

        return path.read_text(encoding="utf-8")
        