import tool_registry
import tools.read_file
import tools.list_directory
from agent import Agent  

registry = tool_registry.ToolRegistry()
registry.register(tools.read_file.ReadFileTool())
registry.register(tools.list_directory.ListDirectoryTool())

agent = Agent(registry)

while True:
    command = input("> ")

    if command == "help":
        print("Available commands:")
        print("  help - Show this help message")
        print("  exit - Exit the program")
        for tool in registry.get_tools():
            print(f"  {tool.name} - {tool.description}")
            print(f"    Usage: {tool.usage}")
    elif command == "exit":
        break
    elif command.startswith("read_file"):
        _, file_path = command.split(maxsplit=1)
        try:
            content = agent.execute("read_file", file_path=file_path)
            print(content)
        except Exception as e:
            print(f"Error: {e}")
    elif command.startswith("list_directory"):
        _, directory_path = command.split(maxsplit=1)
        try:
            contents = agent.execute("list_directory", directory_path=directory_path)
            print(contents)
        except Exception as e:
            print(f"Error: {e}")    
    else:
        print("Unknown command. Type 'help' for a list of available commands.")


print(agent.execute("read_file", file_path="README.md"))
