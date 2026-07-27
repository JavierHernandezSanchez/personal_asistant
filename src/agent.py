class Agent():
    """
    The Agent class is responsible for managing the tools and executing them based on user input.
    It acts as a mediator between the user and the tools, deciding which tool to use based on the input.
    """
    
    def __init__(self, registry):
        self.tool_registry = registry

    def execute(self, tool_name, **kwargs):
        tool = self.tool_registry.get(tool_name)
        if not tool:
            raise ValueError(f"Tool '{tool_name}' not found in the registry.")
        return tool.execute(**kwargs)