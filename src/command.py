from dataclasses import dataclass

@dataclass
class Command:
    """Represents a command to be executed by the agent."""
    tool_name: str | None
    arguments: list[str]