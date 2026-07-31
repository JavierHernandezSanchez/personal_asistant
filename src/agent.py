import shlex
from src.command import Command
from src.tool_registry import ToolRegistry

class Agent():
    """
    The Agent class is responsible for managing the tools and executing them based on user input.
    It acts as a mediator between the user and the tools, deciding which tool to use based on the input.
    """
    
    def __init__(self, registry: ToolRegistry):
        self.tool_registry = registry

    def _parse_input(self, text: str) -> Command:
        """
        Parses the input text and returns a command and its arguments.
        """
        tokens = shlex.split(text)
        if not tokens:
            return Command(tool_name=None, arguments=[])
        command, *args = tokens
        
        return Command(tool_name=command, arguments=args)

    def _show_help(self):
        """
        Displays the help message with available commands and their usage.
        """
        print("Available commands:")
        print("  help - Show this help message")
        print("  exit - Exit the program")
        for tool in self.tool_registry.get_tools():
            print(f"  {tool.name} - {tool.description}")
            print(f"    Usage: {tool.usage}")

    def run(self):
        while True:
            text = input("> ")
            command = self._parse_input(text)            

            if command.tool_name == "help":
                self._show_help()
            elif command.tool_name == "exit":
                break
            else:
                try:
                    tool = self.tool_registry.get(command.tool_name)
                    result = tool.execute(command.arguments)

                    if result is not None:
                        print(result)

                except Exception as e:
                    print(f"Error: {e}")
