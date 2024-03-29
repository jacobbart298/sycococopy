import pyperf
import time
import random
import src.core.instrumentation as asyncio
from src.core.monitor import Monitor
from rps_item import Item

'''
Macro benchmark for Rock-Paper-Scissors that uses a delay instead of picking a random item to ensure
each round is the same. Basline benchmark without monitor
'''

PLAYER_COUNT = 3

def findLosers(playerItems: dict[int: Item]) -> list[int]:
    losers = []
    for player, item in playerItems.items():
        win = False
        lose = False
        for opponent, opponent_item in playerItems.items():
            if player != opponent:
                win = win or item.beats(opponent_item)
                lose = lose or opponent_item.beats(item)
        if lose and not win:
            losers.append(player)
    return losers

async def player(number: int, incoming_queues: dict[int:asyncio.Queue], outgoing_queues: dict[int:asyncio.Queue]):
    round = 1
    is_participating = True
    while is_participating:
        item = Item.random()
        print(f"Player {number} has chosen {item}")
        for queue in outgoing_queues.values():
            await queue.put(item)
        opponent_items = {}
        for player, queue in incoming_queues.items():
            opponent_item = await queue.get()
            opponent_items[player] = opponent_item
        win = False
        lose = False
        tie = False
        for opponent_item in opponent_items.values():
            win = win or item.beats(opponent_item)
            lose = lose or opponent_item.beats(item)
            tie = tie or item == opponent_item
        if win and not lose and not tie:
            if round >=7:
                print(f"Player{number} has won in round {round}!")
            is_participating = False

        elif lose and not win:
            print(f"Player{number} is out of the game!")
            is_participating = False

        else:
            print(f"It's a draw! Player {number} continues to the next round!")
            opponent_items.update({number: item})
            losers = findLosers(opponent_items)
            for loser in losers:
                incoming_queues.pop(loser)
                outgoing_queues.pop(loser)
        round += 1
        await asyncio.sleep(0)
    
async def main():
    random.seed(362)
    queueMap = {}
    for p1 in range(PLAYER_COUNT):
        for p2 in range(PLAYER_COUNT):
            if (p1 != p2):
                queue = asyncio.Queue()
                queueMap[(p1,p2)] = queue
        
    async with asyncio.TaskGroup() as tg:
        for number in range(PLAYER_COUNT):
            incoming_queues = {}
            outgoing_queues = {}
            for (p1, p2) in queueMap.keys():
                if p2 == number:
                    incoming_queues[p1] = queueMap[(p1, p2)]
                if p1 == number:
                    outgoing_queues[p2] = queueMap[(p1, p2)]
            tg.create_task(player(number, incoming_queues, outgoing_queues))

if __name__ == '__main__':
    runner = pyperf.Runner()
    runner.bench_async_func(f"Rock Paper Scissors", main)