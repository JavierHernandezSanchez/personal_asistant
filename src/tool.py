from typing import Any

class Tool():
    name = ""
    description = ""
    usage = ""
    
    def execute(self) -> Any:
        raise NotImplementedError("This method should be overridden by subclasses.")
    

