import random


class HelloWorld:

    def __init__(self, low_api=None):
        self.low_api = low_api

    @staticmethod
    def print_name(name):
        return f"Hello, {name}!"

    @staticmethod
    def random_number(num1, num2):
        return random.randint(int(num1), int(num2))

    @staticmethod
    def run():
        print("hello kernel!")
