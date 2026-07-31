from src.tool import Tool
from pathlib import Path

class CurrentDirectoryTool(Tool):
    """
    Returns the current working directory.

    This tool reports the directory from which the assistant is currently operating.

    It does not change the working directory or inspect its contents.
    """
    name = "current_directory"
    description = "Returns the current working directory."
    usage = "current_directory"
    
    def execute(self, arguments: list[str]) -> str:
        if arguments:
            raise ValueError("No arguments are required.")
        
        return str(Path.cwd())  
