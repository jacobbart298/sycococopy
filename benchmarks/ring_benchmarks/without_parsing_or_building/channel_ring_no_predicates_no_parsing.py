import pyperf
import json
from os import path
from src.core.instrumentation import Channel
import asyncio
from src.core.monitor import Monitor

specification_path = path.abspath("benchmark_specifications/protocol_ring_no_predicates.txt")

async def worker(receiveChannel: Channel, sendChannel: Channel) -> None:
    await receiveChannel.receive()
    await sendChannel.send(True)

async def initiator(receiveChannel: Channel, sendChannel: Channel) -> None:
    await sendChannel.send(True)
    await receiveChannel.receive()

async def main(coroutineCount: int):
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
    monitor.fsm.states = {initialState}
    await main(coroutineCount)

if __name__ == '__main__':
    with open(path.abspath('config.json'), 'r') as config:
        coroutineCount = json.load(config)["ringCount"]
    monitor = Monitor(specification_path)
    initialState = list(monitor.fsm.states)[0]
    runner = pyperf.Runner()
    runner.bench_async_func(f"Coroutine count: {coroutineCount}", runBenchmark)