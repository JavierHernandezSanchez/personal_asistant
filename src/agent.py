from src.command import Command
from src.tool_registry import ToolRegistry
from src.planner import Planner

class Agent():
    """
    The Agent class is responsible for managing the tools and executing them based on user input.
    It acts as a mediator between the user and the tools, deciding which tool to use based on the input.
    """
    
    def __init__(self, registry: ToolRegistry, planner: Planner):
        self.tool_registry = registry
        self.planner = planner

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
        planner = Planner()
        while True:
            text = input("> ")
            command = self.planner.plan(text)

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
