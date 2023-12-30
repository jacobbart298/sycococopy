import src.core.instrumentation as asyncio
from src.core.monitor import Monitor
from rps_item import Item

specification_path = r".\protocol_RPS.txt"
monitor = Monitor(specification_path)

async def player(number: int, outgoing_queues: dict[int:asyncio.Queue], incoming_queues: dict[int:asyncio.Queue]):
    is_participating = True
    while is_participating:
        item = Item.random()
        print(f"Player {number} has chosen {item}")
        for queue in outgoing_queues.values():
            await queue.put(item)
        opponent_items = []
        for queue in incoming_queues.values():
            opponent_item = await queue.get()
            opponent_items.append(opponent_item)
        win = False
        lose = False
        tie = False
        # print(f"Player {number} has the following opponent items {str(opponent_items)}")
        for opponent_item in opponent_items:
            win = win or item.beats(opponent_item)
            lose = lose or opponent_item.beats(item)
            tie = tie or item == opponent_item
        if win and not lose and not tie:
            print(f"Player{number} has won!")
            is_participating = False
        elif lose and not win:
            print(f"Player{number} is out of the game!")
            is_participating = False
            for queue in outgoing_queues.values():
                await queue.put(False)
        else:
            print(f"It's a draw! Player {number} continues to the next round!")
            losers = []
            for queue in outgoing_queues.values():
                await queue.put(True)
            for player, queue in incoming_queues.items():
                if not await queue.get():
                    losers.append(player)
            for loser in losers:
                incoming_queues.pop(loser)
                outgoing_queues.pop(loser)
        await asyncio.sleep(0.5)
    
async def main(player_count: int):
    queueMap = {}
    for p1 in range(player_count):
        for p2 in range(player_count):
            if (p1 != p2):
                queue = asyncio.Queue()
                asyncio.link(queue, f"Player{p1}", f"Player{p2}", monitor)
                queueMap[(p1,p2)] = queue
        
    async with asyncio.TaskGroup() as tg:
        for number in range(player_count):
            incoming_queues = {}
            outgoing_queues = {}
            for (p1, p2) in queueMap.keys():
                if p2 == number:
                    incoming_queues[p1] = queueMap[(p1, p2)]
                if p1 == number:
                    outgoing_queues[p2] = queueMap[(p1, p2)]
            tg.create_task(player(number, incoming_queues, outgoing_queues))

asyncio.run(main(3))