import datetime


class Commands:
    def __init__(self):
        self.commands = []

    def set_commands(self, req_content: dict) -> list:
        self.commands = req_content['commands']
        return self.commands

    def set_commands_unique(self, req_content: dict) -> list:
        res = []
        for command in req_content['commands']:
            if command not in res:
                res.append(command)
        self.commands = res
        return self.commands

    def get_commands(self) -> list:
        return self.commands

    def get_commands_unique(self) -> list:
        res = []
        for c in self.commands:
            if c not in res:
                res.append(c)
        return res
