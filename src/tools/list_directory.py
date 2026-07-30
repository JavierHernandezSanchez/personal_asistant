from src.tool import Tool
from pathlib import Path

class ListDirectoryTool(Tool):
    name = "list_directory"
    description = "Lists the contents of a specified directory."
    usage = "list_directory <directory_path>"
    
    def execute(self, directory_path: str) -> str:
        path = Path(directory_path)
        if not path.exists():
            raise FileNotFoundError(f"Directory '{directory_path}' does not exist.")
        if not path.is_dir():
            raise NotADirectoryError(f"'{directory_path}' is not a directory.") 
        
        contents = sorted([item.name for item in path.iterdir()])
        return "\n".join(contents)
        