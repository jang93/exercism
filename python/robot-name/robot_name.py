import random
import string


class Robot:
    def __init__(self):
        self.name = self.get_random_name()

    def reset(self):
        random.seed(self.name)
        self.name = self.get_random_name()

    @staticmethod
    def get_random_name():
        return ''.join(random.choices(string.ascii_uppercase, k=2) + random.choices(string.digits, k=3))

