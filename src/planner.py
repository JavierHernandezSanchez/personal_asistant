from src.command import Command
import shlex

class Planner():
    """
    The Planner converts user input into a Command.
    """

    def plan(self, text: str) -> Command:
        """
        Parses the input text and returns a command and its arguments.
        """
        tokens = shlex.split(text)
        if not tokens:
            return Command(tool_name=None, arguments=[])
        command, *args = tokens
        
        return Command(tool_name=command, arguments=args)