from enum import Enum
import random

class Item(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def beats(self, other):
        return ((self == Item.ROCK and other == Item.SCISSORS) 
                or (self == Item.PAPER and other == Item.ROCK) 
                or (self == Item.SCISSORS and other == Item.PAPER))

    @staticmethod
    def random():
        return random.choice(list(Item))