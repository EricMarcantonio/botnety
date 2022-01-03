from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import base64


class Commands:
    def __init__(self):
        self.commands = []

    def set_commands(self, req_content: dict) -> list:
        self.commands = req_content['command']
        return self.commands

    def set_commands_unique(self, req_content: dict) -> list:
        res = []
        for command in req_content['command']:
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

    def get_commands_encrypted_unique(self):
        res = []
        for c in self.commands:
            if c not in res:
                res.append(c)
        res_str = ';'.join(res)
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(res_str.encode())
        ciphertext = base64.urlsafe_b64encode(ciphertext).decode("utf-8")
        tag = base64.urlsafe_b64encode(tag).decode("utf-8")
        key = base64.urlsafe_b64encode(key).decode("utf-8")
        return ciphertext, tag, key

