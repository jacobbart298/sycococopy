import typing
import pyperf
from benchmarks.config import coroutineCount
import asyncio
from asyncio import Queue


print(f"Starting benchmark for {coroutineCount} coroutines")

async def worker(receiveQueue: Queue, sendQueue: Queue, number: int) -> None:
    await receiveQueue.get()
    await sendQueue.put(True)
    print(f"Coroutine{number} sent a message")

async def initiator(receiveQueue: Queue, sendQueue: Queue) -> None:
    await sendQueue.put(True)
    print("Coroutine0 sent a message")
    await receiveQueue.get()

async def main(coroutineCount: int):
    async with asyncio.TaskGroup() as tg:
        sender = "coroutine0"
        receiver = "coroutine1"
        sendQueue = Queue()
        initialReceiveQueue = Queue()
        # create first worker
        tg.create_task(initiator(initialReceiveQueue, sendQueue))
        # create second worker - penultimate worker
        for i in range(1, coroutineCount-1):
            sender = f"coroutine{i}"
            receiver = f"coroutine{i + 1}"
            receiveQueue = sendQueue
            sendQueue = Queue()           
            tg.create_task(worker(receiveQueue, sendQueue, i))
        # create last worker
        sender = f"coroutine{coroutineCount-1}"
        receiver = "coroutine0"
        receiveQueue = sendQueue
        sendQueue = initialReceiveQueue
        tg.create_task(worker(receiveQueue, sendQueue, coroutineCount-1))
        print("started")
    print("finished")

async def runBenchmark() -> None:
    await main(coroutineCount)

runner = pyperf.Runner()
runner.bench_async_func(f"Benchmark {coroutineCount}", runBenchmark)