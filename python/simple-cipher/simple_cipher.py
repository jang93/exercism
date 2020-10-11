import secrets
import string
from string import ascii_lowercase


class Cipher:
    def __init__(self, key=None):
        self.key = key if key is not None else ''.join([secrets.choice(string.ascii_lowercase) for _ in range(100)])

    def encode(self, text):
        return ''.join([chr((ord(letter) + (ord(self.key[ind % len(self.key)])-97) - 97) % 26 + 97) for ind, letter in enumerate(text)])

    def decode(self, text):
        return ''.join([chr((ord(letter) - (ord(self.key[ind % len(self.key)])-97) - 97) % 26 + 97) for ind, letter in enumerate(text)])

