from .tool_registry import ToolRegistry
from .tools.read_file import ReadFileTool
from .tools.list_directory import ListDirectoryTool
from .tools.current_directory import CurrentDirectoryTool
from .tools.write_file import WriteFileTool
from .agent import Agent


def main():
    registry = ToolRegistry()
    registry.register(ReadFileTool())
    registry.register(ListDirectoryTool())
    registry.register(WriteFileTool())
    registry.register(CurrentDirectoryTool())

    agent = Agent(registry)
    agent.run()


if __name__ == "__main__":
    main()