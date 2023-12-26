import pyperf
import json
from os import path
from src.core.instrumentation import Queue
import src.core.instrumentation as asyncio
from src.core.monitor import Monitor

specification_path = path.abspath("benchmark_specifications/protocol_tree_no_predicates.txt")

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
        workerA = "A"
        workerB = "B"
        queueAtoB = Queue()
        queueBtoA = Queue()
        asyncio.link(queueAtoB, workerA, workerB, monitor)
        asyncio.link(queueBtoA, workerB, workerA, monitor)
        tg.create_task(A(queueBtoA, queueAtoB, depth))
        tg.create_task(B(queueAtoB, queueBtoA, depth))

async def runBenchmark() -> None:
    monitor.fsm.states = {initialState}
    await main(level)

if __name__ == '__main__':
    with open(path.abspath('config.json'), 'r') as config:
        level = json.load(config)["nddepth"]
    monitor = Monitor(specification_path)
    initialState = list(monitor.fsm.states)[0]
    runner = pyperf.Runner()
    runner.bench_async_func(f"Benchmark {level}", runBenchmark)