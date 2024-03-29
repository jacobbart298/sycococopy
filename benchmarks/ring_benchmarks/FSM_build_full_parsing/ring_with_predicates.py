import pyperf
import json
from os import path
from src.core.instrumentation import Queue
import src.core.instrumentation as asyncio
from src.core.monitor import Monitor

'''
Ring benchmark where coroutines forward messages in a ring until intial coroutine is reached.
Benchmark with full parsing.
'''

specification_path = path.abspath("benchmark_specifications/protocol_ring_with_predicates.txt")

def writeSpecification(coroutineCount: int) -> None:
    specification : str = ""
    # write role header
    specification += "roles:\n"
    # write roles
    for i in range(coroutineCount):
        specification += f"\tcoroutine{i}\n"
    # write protocol header
    specification += "\nprotocol:\n"
    # write sequence expression
    specification += "\tsequence:\n"
    # write sends
    for i in range(coroutineCount-1):
        specification += f"\t\tsend bool(True) from coroutine{i} to coroutine{i+1}\n"
    specification += f"\t\tsend bool(True) from coroutine{coroutineCount-1} to coroutine{0}"

    with open(specification_path, 'w') as spec:
        spec.write(specification)

async def worker(receiveQueue: Queue, sendQueue: Queue) -> None:
    await receiveQueue.get()
    await sendQueue.put(True)

async def initiator(receiveQueue: Queue, sendQueue: Queue) -> None:
    await sendQueue.put(True)
    await receiveQueue.get()

async def main(coroutineCount: int):
    monitor = Monitor(specification_path)
    async with asyncio.TaskGroup() as tg:
        sender = "coroutine0"
        receiver = "coroutine1"
        sendQueue = Queue()
        initialReceiveQueue = Queue()
        asyncio.link(sendQueue, sender, receiver, monitor)
        # create first worker
        tg.create_task(initiator(initialReceiveQueue, sendQueue))
        # create second worker - penultimate worker
        for i in range(1, coroutineCount-1):
            sender = f"coroutine{i}"
            receiver = f"coroutine{i + 1}"
            receiveQueue = sendQueue
            sendQueue = Queue()
            asyncio.link(sendQueue, sender, receiver, monitor)            
            tg.create_task(worker(receiveQueue, sendQueue))
        # create last worker
        sender = f"coroutine{coroutineCount-1}"
        receiver = "coroutine0"
        receiveQueue = sendQueue
        sendQueue = initialReceiveQueue
        asyncio.link(sendQueue, sender, receiver, monitor)
        tg.create_task(worker(receiveQueue, sendQueue))

async def runBenchmark() -> None:
    await main(coroutineCount)

if __name__ == '__main__':
    with open(path.abspath('config.json'), 'r') as config:
        coroutineCount = json.load(config)["ringCount"]
    runner = pyperf.Runner()
    runner.bench_async_func(f"Coroutine count: {coroutineCount}", runBenchmark)