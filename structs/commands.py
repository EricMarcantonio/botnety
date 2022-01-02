import datetime


class Commands:
    def __init__(self):
        self.commands = []

    def set_commands(self, req_content: dict) -> list:
        for _id, command in req_content.items():
            self.commands.append(command)
        return self.commands

    def set_commands_unique(self, req_content: dict) -> list:
        for _id, command in req_content.items():
            if command not in self.commands:
                self.commands.append(command)
        return self.commands

    def get_commands(self) -> list:
        return self.commands

    def get_commands_unique(self) -> list:
        res = []
        for c in self.commands:
            if c not in res:
                res.append(c)
        return res
