import pyperf
from os import path
import src.core.instrumentation as asyncio
from src.core.monitor import Monitor
from rps_item import Item

PLAYER_COUNT = 3
specification_path = r".\protocol_RPS.txt"
monitor = Monitor(specification_path, enforceCausality=False)

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


async def player(number: int, incoming_queues: dict[int:asyncio.Queue], outgoing_queues: dict[int:asyncio.Queue], item_list: list[Item]):
    is_participating = True
    while is_participating:
        item = item_list.pop()
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
            print(f"Player{number} has won!")
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
        await asyncio.sleep(1.5/1000000)
    
async def main():
    queueMap = {}
    item_list_p1 = [Item.ROCK, Item.SCISSORS, Item.PAPER, Item.ROCK, Item.PAPER, Item.SCISSORS, Item.PAPER, Item.ROCK]
    item_list_p2 = [Item.SCISSORS, Item.SCISSORS, Item.PAPER, Item.ROCK, Item.PAPER, Item.ROCK, Item.SCISSORS, Item.PAPER]
    item_list_p3 = [Item.ROCK, Item.PAPER, Item.ROCK, Item.SCISSORS]
    item_lists = [item_list_p3, item_list_p2, item_list_p1]
    for p1 in range(PLAYER_COUNT):
        for p2 in range(PLAYER_COUNT):
            if (p1 != p2):
                queue = asyncio.Queue()
                asyncio.link(queue, f"Player{p1}", f"Player{p2}", monitor)
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
            tg.create_task(player(number, incoming_queues, outgoing_queues, item_lists.pop()))


if __name__ == '__main__':
    runner = pyperf.Runner()
    runner.bench_async_func(f"Rock Paper Scissors", main)