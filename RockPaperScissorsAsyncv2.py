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
    task1 = asyncio.create_task(player(1))
    task2 = asyncio.create_task(player(2))
    task3 = asyncio.create_task(player(3))
    item1 = await task1
    item2 = await task2
    item3 = await task3

asyncio.run(main())