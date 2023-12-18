import pyperf
from benchmarks.config import level
from asyncio import Queue
import asyncio

async def A(queueBtoA: Queue, queueAtoB: Queue, level: int) -> None:
    while level > 0:
        await queueAtoB.put(True)
        if level > 1:
            await queueBtoA.get()
        level -= 2

async def B(queueAtoB: Queue, queueBtoA: Queue, level: int) -> None:
    while level > 1:
        await queueAtoB.get()
        level -= 2
        await queueBtoA.put(False)
    if level%2 == 1:
        await queueAtoB.get()

async def main(depth: int):
    async with asyncio.TaskGroup() as tg:
        queueAtoB = Queue()
        queueBtoA = Queue()
        tg.create_task(A(queueBtoA, queueAtoB, depth))
        tg.create_task(B(queueAtoB, queueBtoA, depth))

async def runBenchmark() -> None:
    await main(level)

if __name__ == '__main__':
    runner = pyperf.Runner()
    runner.bench_async_func(f"Benchmark {level}", runBenchmark)