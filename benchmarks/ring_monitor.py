import pyperf
from benchmarks.config import coroutineCount
from src.core.instrumentation import Queue
import src.core.instrumentation as asyncio
from src.core.monitor import Monitor

specification_path = r".\ring_monitor_protocol.txt"

def writeSpecification(coroutineCount: int) -> None:
    specification : str = ""
    # write role header
    specification += "roles:\n"
    # write roles
    for i in range(coroutineCount):
        specification += f"    coroutine{i}\n"
    # write protocol header
    specification += "\nprotocol:\n"
    # write sequence expression
    specification += "    sequence:\n"
    # write sends
    for i in range(coroutineCount-1):
        specification += f"        send bool from coroutine{i} to coroutine{i+1}\n"
    specification += f"        send bool from coroutine{coroutineCount-1} to coroutine{0}"

    with open(r'.\ring_monitor_protocol.txt', 'w') as spec:
        spec.write(specification)

async def worker(receiveQueue: Queue, sendQueue: Queue) -> None:
    await receiveQueue.get()
    await sendQueue.put(True)

async def initiator(receiveQueue: Queue, sendQueue: Queue) -> None:
    await sendQueue.put(True)
    await receiveQueue.get()

async def main(coroutineCount: int):
    monitor = Monitor(specification_path)
    async with asyncio.TaskGroup() as tg:
        sender = "coroutine0"
        receiver = "coroutine1"
        sendQueue = Queue()
        initialReceiveQueue = Queue()
        asyncio.link(sendQueue, sender, receiver, monitor)
        # create first worker
        tg.create_task(initiator(initialReceiveQueue, sendQueue))
        # create second worker - penultimate worker
        for i in range(1, coroutineCount-1):
            sender = f"coroutine{i}"
            receiver = f"coroutine{i + 1}"
            receiveQueue = sendQueue
            sendQueue = Queue()
            asyncio.link(sendQueue, sender, receiver, monitor)            
            tg.create_task(worker(receiveQueue, sendQueue))
        # create last worker
        sender = f"coroutine{coroutineCount-1}"
        receiver = "coroutine0"
        receiveQueue = sendQueue
        sendQueue = initialReceiveQueue
        asyncio.link(sendQueue, sender, receiver, monitor)
        tg.create_task(worker(receiveQueue, sendQueue))


writeSpecification(coroutineCount)

async def runBenchmark() -> None:
    await main(coroutineCount)

runner = pyperf.Runner()
runner.bench_async_func(f"Benchmark {coroutineCount}", runBenchmark)