import pyperf
from antlr4 import FileStream, CommonTokenStream
from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.PythonicParser import PythonicParser
from benchmarks.config import loopCount
from src.core.instrumentation import Queue
import src.core.instrumentation as asyncio
from benchmarks.benchmark_monitor import BenchmarkMonitor

specification_path = r".\protocol_loop_no_predicates.txt"

def writeSpecification() -> None:
    indent = '\t'
    specification : str = ""
    # write role header and roles
    specification += f"roles:\n{indent}A\n{indent}B\n"
    # write protocol header
    specification += "\nprotocol:\n"
    # start loop
    specification += indent + "loop start:\n"
    # sequence with choice to loop or send and end
    specification += 2 * indent + "choice:\n"
    specification += 3 * indent + "sequence:\n"
    specification += 4 * indent + "send int from A to B\n"
    specification += 4 * indent + "send int from B to A\n"
    specification += 4 * indent + "repeat start\n"
    specification += 3 * indent + "send int from A to B\n"

    with open(specification_path, 'w') as spec:
        spec.write(specification)

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
        monitor = BenchmarkMonitor(parseTree)
        workerA = "A"
        workerB = "B"
        queueAtoB = Queue()
        queueBtoA = Queue()
        asyncio.link(queueAtoB, workerA, workerB, monitor)
        asyncio.link(queueBtoA, workerB, workerA, monitor)
        tg.create_task(A(queueBtoA, queueAtoB, loopCount))
        tg.create_task(B(queueAtoB, queueBtoA, loopCount))

# Parses the given specification in the filePath to a parse tree.
def buildParseTree(filePath: str):
    input = FileStream(filePath)
    lexer = PythonicLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PythonicParser(stream)
    return parser.specification()

async def runBenchmark() -> None:
    await main(loopCount)

parseTree = buildParseTree(specification_path)
runner = pyperf.Runner()
runner.bench_async_func(f"Loopcount: {loopCount}", runBenchmark)