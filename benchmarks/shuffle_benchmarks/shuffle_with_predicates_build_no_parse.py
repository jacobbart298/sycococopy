import pyperf
from antlr4 import FileStream, CommonTokenStream
from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.PythonicParser import PythonicParser
from benchmarks.config import starWorkers
from src.core.instrumentation import Queue
import src.core.instrumentation as asyncio
from benchmarks.benchmark_monitor import BenchmarkMonitor

'''
A benchmark that performs one-to-many send operations (star send).
The order predetermined to ensure repeatability of the benchmark.
This tests the sycococopy shuffle operator with predicates. 
'''

specification_path = r".\protocol_shuffle_with_predicates.txt"

def writeSpecification(workerCount: int) -> None:
    indent = "\t"
    specification : str = ""
    # write role header
    specification += "roles:\n"
    specification += indent + "main\n"
    # write roles
    for i in range(1, workerCount+1):
        specification += indent + f"worker{i}\n"
        # print(f"Worker {i} created")
    # write protocol header
    specification += "\nprotocol:\n"
    # write sequence expression
    specification += indent + "shuffle:\n"
    # write sends
    for i in range(1, workerCount+1):
        # print(f"send from main to worker {i} in protocol")
        specification += 2*indent + f'send str(>"C") from main to worker{i}\n'

    with open(specification_path, 'w') as spec:
        spec.write(specification)
        spec.close()

async def worker(receiveQueue: Queue) -> None:
    await receiveQueue.get()

async def center(sendQueues: list[Queue], workerCount: int) -> None:
    for i in range(workerCount-1, -1, -1):
        await sendQueues[i].put("Check this out!")

async def main(workerCount: int) -> None:
    monitor = BenchmarkMonitor(parseTree)
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

# Parses the given specification in the filePath to a parse tree.
def buildParseTree(filePath: str):
    input = FileStream(filePath)
    lexer = PythonicLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PythonicParser(stream)
    return parser.specification() 

async def runBenchmark() -> None:
    await main(starWorkers)

if __name__ == '__main__':
    writeSpecification(starWorkers)
    parseTree = buildParseTree(specification_path)
    runner = pyperf.Runner()
    runner.bench_async_func(f"Worker count: {starWorkers}", runBenchmark)