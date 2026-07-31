from .tool_registry import ToolRegistry
from .tools.read_file import ReadFileTool
from .tools.list_directory import ListDirectoryTool
from .tools.current_directory import CurrentDirectoryTool
from .tools.change_directory import ChangeDirectoryTool
from .tools.write_file import WriteFileTool
from .tools.delete_file import DeleteFileTool
from .agent import Agent


def main():
    registry = ToolRegistry()
    registry.register(ReadFileTool())
    registry.register(ListDirectoryTool())
    registry.register(WriteFileTool())
    registry.register(CurrentDirectoryTool())
    registry.register(ChangeDirectoryTool())
    registry.register(DeleteFileTool())

    agent = Agent(registry)
    agent.run()


if __name__ == "__main__":
    main()