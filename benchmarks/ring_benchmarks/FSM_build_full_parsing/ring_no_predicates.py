import pyperf
import json
from os import path
from src.core.instrumentation import Queue
import src.core.instrumentation as asyncio
from src.core.monitor import Monitor

specification_path = path.abspath("benchmark_specifications/protocol_ring_no_predicates.txt")

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