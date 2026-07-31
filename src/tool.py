from typing import Any

class Tool():
    name = ""
    description = ""
    usage = ""
    
    def execute(self, arguments: list[str]) -> Any:
        raise NotImplementedError("This method should be overridden by subclasses.")
    

