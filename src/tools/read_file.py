from tool import Tool
class ReadFileTool(Tool):
    """
    Reads the content of a specified file.

    This tool is responsible for opening a text file and returning its content as a string.

    It does not parse, summarize, validate or modify the file.
    """

    name = "read_file"
    description = "Reads the content of a specified file."
    
    def execute(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        except Exception as e:
            return f"Error reading file: {e}"