import pyperf
import json
from os import path
import asyncio
from asyncio import Queue

async def worker(receiveQueue: Queue, sendQueue: Queue) -> None:
    await receiveQueue.get()
    await sendQueue.put(True)

async def initiator(receiveQueue: Queue, sendQueue: Queue) -> None:
    await sendQueue.put(True)
    await receiveQueue.get()

async def main(coroutineCount: int):
    async with asyncio.TaskGroup() as tg:
        sendQueue = Queue()
        initialReceiveQueue = Queue()
        # create first worker
        tg.create_task(initiator(initialReceiveQueue, sendQueue))
        # create second worker - penultimate worker
        for _ in range(1, coroutineCount-1):
            receiveQueue = sendQueue
            sendQueue = Queue()           
            tg.create_task(worker(receiveQueue, sendQueue))
        # create last worker
        receiveQueue = sendQueue
        sendQueue = initialReceiveQueue
        tg.create_task(worker(receiveQueue, sendQueue))

async def runBenchmark() -> None:
    await main(coroutineCount)

if __name__ == '__main__':
    with open(path.abspath('config.json'), 'r') as config:
        coroutineCount = json.load(config)["ringCount"]
    runner = pyperf.Runner()
    runner.bench_async_func(f"Coroutine count: {coroutineCount}", runBenchmark)