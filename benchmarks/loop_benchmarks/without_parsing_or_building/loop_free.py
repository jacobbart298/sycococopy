import pyperf
from benchmarks.config import loopCount
from asyncio import Queue
import asyncio

async def A(receiveQueue: Queue, sendQueue: Queue, loopCount: int) -> None:
    while loopCount > 0:
        await sendQueue.put(1)
        await receiveQueue.get()
        loopCount -= 1
    await sendQueue.put(0)

async def B(receiveQueue: Queue, sendQueue: Queue, loopCount: int) -> None:
    while loopCount > 0:
        await receiveQueue.get()
        await sendQueue.put(0)
        loopCount -= 1
    await receiveQueue.get()

async def main(loopCount: int):
    async with asyncio.TaskGroup() as tg:
        queueAtoB = Queue()
        queueBtoA = Queue()
        tg.create_task(A(queueBtoA, queueAtoB, loopCount))
        tg.create_task(B(queueAtoB, queueBtoA, loopCount))

async def runBenchmark() -> None:
    await main(loopCount)

if __name__ == '__main__':
    runner = pyperf.Runner()
    runner.bench_async_func(f"Loopcount: {loopCount}", runBenchmark)