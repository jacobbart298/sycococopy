import pyperf
import json
from os import path
from src.core.instrumentation import Channel
import asyncio
from benchmarks.benchmark_monitor import BenchmarkMonitor
from benchmarks.benchmarkmethods import buildParseTree

'''
Ring benchmark where coroutines forward messages in a ring until intial coroutine is reached.
CHANNEL Benchmark without parsing but with building of the fsm.
'''

specification_path = path.abspath("benchmark_specifications/protocol_ring_no_predicates.txt")

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