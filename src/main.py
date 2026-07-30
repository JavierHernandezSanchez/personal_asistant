from .tool_registry import ToolRegistry
from .tools.read_file import ReadFileTool
from .tools.list_directory import ListDirectoryTool
from .tools.write_file import WriteFileTool
from .agent import Agent  

def main():
    registry = ToolRegistry()
    registry.register(ReadFileTool())
    registry.register(ListDirectoryTool())
    registry.register(WriteFileTool())

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
        elif command.startswith("write_file"):
            parts = command.split(maxsplit=2)
            if len(parts) < 3:
                print("Error: Missing arguments. Usage: write_file <file_path> <content>")
                continue
            _, file_path, content = parts
            try:
                agent.execute("write_file", file_path=file_path, content=content)
                print(f"Content written to '{file_path}' successfully.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Unknown command. Type 'help' for a list of available commands.")


if __name__ == "__main__":
    main()