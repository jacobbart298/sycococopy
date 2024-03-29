import pyperf
import json
from os import path
from src.core.instrumentation import Queue
import src.core.instrumentation as asyncio
from src.core.monitor import Monitor

'''
A benchmark that performs one-to-many send operations (star send).
The order predetermined to ensure repeatability of the benchmark.
This tests the sycococopy shuffle operator with predicates. 
'''

specification_path = path.abspath("benchmark_specifications/protocol_shuffle_with_predicates.txt")

async def worker(receiveQueue: Queue) -> None:
    await receiveQueue.get()

async def center(sendQueues: list[Queue], workerCount: int) -> None:
    for i in range(workerCount-1, -1, -1):
        await sendQueues[i].put("Check this out!")

async def main(workerCount: int) -> None:
    monitor = Monitor(specification_path)
    async with asyncio.TaskGroup() as tg:
        sender: str = "main"
        queueList: list[Queue] = []
        for i in range(1, workerCount+1):
            receiver = f"worker{i}"
            queue = Queue()
            queueList.append(queue)
            asyncio.link(queue, sender, receiver, monitor)           
            tg.create_task(worker(queue))
        tg.create_task(center(queueList, workerCount))

async def runBenchmark() -> None:
    await main(starWorkers)

if __name__ == '__main__':
    with open(path.abspath('config.json'), 'r') as config:
        starWorkers = json.load(config)["shuffleCount"]
    runner = pyperf.Runner()
    runner.bench_async_func(f"Worker count: {starWorkers}", runBenchmark)