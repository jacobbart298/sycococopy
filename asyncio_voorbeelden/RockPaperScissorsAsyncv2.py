import asyncio
import random
from enum import Enum

class Item(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def beats(self, item2):
        return ((self == Item.ROCK and item2 == Item.SCISSORS) 
                or (self == Item.PAPER and item2 == Item.ROCK) 
                or (self == Item.SCISSORS and item2 == Item.PAPER))

    @staticmethod
    def random():
        return random.choice(list(Item))

item = Item.random()
beats = item.beats(Item.SCISSORS)
print(f'You chose {item}, which beats Scissors = {beats}')

async def player(number):
    print(f'player {number} has started')
    await asyncio.sleep(2)
    item = Item.random()
    print(f'player {number} returns {item}')
    return item

async def main():
    async with asyncio.TaskGroup() as tg:
        for number in range(3):
            tg.create_task(player(number))

asyncio.run(main())