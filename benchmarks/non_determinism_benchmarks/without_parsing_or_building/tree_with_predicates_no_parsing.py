import pyperf
import cProfile
import re
from benchmarks.config import level
from src.core.instrumentation import Queue
import src.core.instrumentation as asyncio
from src.core.monitor import Monitor

specification_path = r".\protocol_tree_with_predicates.txt"

def writeSpecification(level: int) -> None:
    indent = "\t"
    specification = "roles:\n"
    specification += indent + "A\n"
    specification += indent + "B\n"
    specification += "\nprotocol:\n"
    specification += indent + "choice:\n"
    specification += writeProtocol(1, 2, level, True)
    specification += writeProtocol(1, 2, level, False)

    with open(specification_path, 'w') as spec:
        spec.write(specification)

# recursive method to write increasingly deep choice protocol with binary tree result
def writeProtocol(depth: int, indentLevel: int, maxDepth: int, value: bool) -> str:
    indent = "\t"
    if depth == maxDepth and depth % 2 == 1:
        return indentLevel*indent + f"send bool({value}) from A to B\n"
    elif depth == maxDepth and depth % 2 == 0:
        return indentLevel*indent + f"send bool({value}) from B to A\n"
    else:
        protocol = indentLevel*indent + "sequence:\n"
        indentLevel += 1
        if depth % 2 == 1:
            protocol += indentLevel*indent + f"send bool({value}) from A to B\n"
        else:
            protocol += indentLevel*indent + f"send bool({value}) from B to A\n"
        protocol += indentLevel*indent + "choice:\n"
        protocol += writeProtocol(depth + 1, indentLevel + 1, maxDepth, value)
        protocol += writeProtocol(depth + 1, indentLevel + 1, maxDepth, not value)
        return protocol

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
    writeSpecification(level)
    monitor = Monitor(specification_path)
    initialState = list(monitor.fsm.states)[0]
    runner = pyperf.Runner()
    runner.bench_async_func(f"Benchmark {level}", runBenchmark)