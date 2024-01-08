import pyperf
import json
from os import path
from src.core.instrumentation import Channel
import asyncio
from benchmarks.benchmarkmethods import buildParseTree
from benchmarks.benchmark_monitor import BenchmarkMonitor

specification_path = path.abspath("benchmark_specifications/protocol_ring_with_predicates.txt")

def writeSpecification(coroutineCount: int) -> None:
    specification : str = ""
    # write role header
    specification += "roles:\n"
    # write roles
    for i in range(coroutineCount):
        specification += f"\tcoroutine{i}\n"
    # write protocol header
    specification += "\nprotocol:\n"
    # write sequence expression
    specification += "\tsequence:\n"
    # write sends
    for i in range(coroutineCount-1):
        specification += f"\t\tsend bool(True) from coroutine{i} to coroutine{i+1}\n"
    specification += f"\t\tsend bool(True) from coroutine{coroutineCount-1} to coroutine{0}"

    with open(specification_path, 'w') as spec:
        spec.write(specification)

async def worker(receiveChannel: Channel, sendChannel: Channel) -> None:
    await receiveChannel.receive()
    await sendChannel.send(True)

async def initiator(receiveChannel: Channel, sendChannel: Channel) -> None:
    await sendChannel.send(True)
    await receiveChannel.receive()

async def main(coroutineCount: int):
    monitor = BenchmarkMonitor(parseTree)
    async with asyncio.TaskGroup() as tg:
        initialSender = "coroutine0"
        receiver = "coroutine1"
        finalSender = f"coroutine{coroutineCount-1}"
        sendChannel = Channel(initialSender, receiver, monitor)
        initialReceiveChannel = Channel(finalSender, initialSender, monitor)
        tg.create_task(initiator(initialReceiveChannel, sendChannel))
        for i in range(1, coroutineCount-1):
            sender = f"coroutine{i}"
            receiver = f"coroutine{i + 1}"
            receiveChannel = sendChannel
            sendChannel = Channel(sender, receiver, monitor)          
            tg.create_task(worker(receiveChannel, sendChannel))
        # create last worker
        sender = f"coroutine{coroutineCount-1}"
        receiver = "coroutine0"
        receiveChannel = sendChannel
        sendChannel = initialReceiveChannel
        tg.create_task(worker(receiveChannel, sendChannel))

async def runBenchmark() -> None:
    await main(coroutineCount)

if __name__ == '__main__':
    with open(path.abspath('config.json'), 'r') as config:
        coroutineCount = json.load(config)["ringCount"]
    parseTree = buildParseTree(specification_path)
    runner = pyperf.Runner()
    runner.bench_async_func(f"Coroutine count: {coroutineCount}", runBenchmark)