import tool_registry
import tools.read_file
from agent import Agent  

registry = tool_registry.ToolRegistry()
registry.register(tools.read_file.ReadFileTool())

agent = Agent(registry)

while True:
    command = input("> ")

    if command == "help":
        print("Available commands:")
        print("  help - Show this help message")
        print("  exit - Exit the program")
        for tool in registry.get_tools():
            print(f"  {tool.name} - {tool.description}")        
    elif command == "exit":
        break
    elif command.startswith("read_file"):
        _, file_path = command.split(maxsplit=1)
        try:
            content = agent.execute("read_file", file_path=file_path)
            print(content)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Unknown command. Type 'help' for a list of available commands.")


print(agent.execute("read_file", file_path="README.md"))
