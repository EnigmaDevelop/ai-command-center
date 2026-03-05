from src.tools.web_request import fetch_url

class Agent:
    def run(self, command: str) -> str:
        if not command:
            return "No command provided."

        command = command.strip()

        # If the command is a URL → use fetch_url tool
        if command.startswith("http://") or command.startswith("https://"):
            return fetch_url(command)

        # Otherwise perform a simple echo-style action
        return f"Agent executed command: {command}"
