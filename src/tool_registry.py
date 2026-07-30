from src.tool import Tool
class ToolRegistry:
    """
    Stores and provides access to the tools available to the assistant.

    It wont execute tools or decide which tool to use.
    """

    def __init__(self):
        self._tools: dict[str, Tool] = {}    

    def register(self, tool: Tool) -> None:
        """
        Registers a new tool in the registry.

        Args:
            tool (Tool): The tool instance to be registered.

        Raises:
            ValueError: If a tool with the same name is already registered.
        """
        if tool.name in self._tools:
            raise ValueError(f"Tool '{tool.name}' is already registered.")
        self._tools[tool.name] = tool

    def get(self, tool_name: str) -> Tool:
        """
        Retrieves a tool by its name.

        Args:
            tool_name (str): The name of the tool to retrieve.

        Returns:
            Tool: The tool instance associated with the given name.

        Raises:
            KeyError: If the tool is not registered.
        """
        if tool_name not in self._tools:
            raise KeyError(f"Tool '{tool_name}' is not registered.")
        return self._tools[tool_name]

    def has(self, tool_name: str) -> bool:
        """
        Checks if a tool is registered.

        Args:
            tool_name (str): The name of the tool to check.

        Returns:
            bool: True if the tool is registered, False otherwise.
        """
        return tool_name in self._tools

    def get_tools(self) -> list[Tool]:
        """
        Retrieves all registered tools.

        Returns:
            List[Tool]: A list of all registered tool instances.
        """
        return list(self._tools.values())