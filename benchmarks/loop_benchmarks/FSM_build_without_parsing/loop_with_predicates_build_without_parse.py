import pyperf
import json
from os import path
from benchmarks.benchmarkmethods import buildParseTree
from src.core.instrumentation import Queue
import src.core.instrumentation as asyncio
from benchmarks.benchmark_monitor import BenchmarkMonitor

'''
Loop benchmarks where two coroutines send messages back and forth for a
number of times. Test without parsing but with building of the fsm.
'''

specification_path = path.abspath("benchmark_specifications/protocol_loop_with_predicates.txt")

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
    monitor = BenchmarkMonitor(parseTree)
    async with asyncio.TaskGroup() as tg:
        workerA = "A"
        workerB = "B"
        queueAtoB = Queue()
        queueBtoA = Queue()
        asyncio.link(queueAtoB, workerA, workerB, monitor)
        asyncio.link(queueBtoA, workerB, workerA, monitor)
        tg.create_task(A(queueBtoA, queueAtoB, loopCount))
        tg.create_task(B(queueAtoB, queueBtoA, loopCount))

async def runBenchmark() -> None:
    await main(loopCount)

if __name__ == '__main__':
    with open(path.abspath('config.json'), 'r') as config:
        loopCount = json.load(config)["loopCount"]
    parseTree = buildParseTree(specification_path)
    runner = pyperf.Runner()
    runner.bench_async_func(f"Loopcount: {loopCount}", runBenchmark)