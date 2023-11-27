import typing
import pyperf
from src.core.instrumentation import Queue
import src.core.instrumentation as asyncio
from src.core.monitor import Monitor


specification_path = r".\var_coroutines_protocol.txt"

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

    with open(r'.\var_coroutines_protocol.txt', 'w') as spec:
        spec.write(specification)

async def worker(receiveQueue: Queue, sendQueue: Queue, number: int) -> None:
    await receiveQueue.get()
    await sendQueue.put(True)
    print(f"Coroutine{number} sent a message")

async def initiator(receiveQueue: Queue, sendQueue: Queue) -> None:
    await sendQueue.put(True)
    print("Coroutine0 sent a message")
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
            tg.create_task(worker(receiveQueue, sendQueue, i))
        # create last worker
        sender = f"coroutine{coroutineCount-1}"
        receiver = "coroutine0"
        receiveQueue = sendQueue
        sendQueue = initialReceiveQueue
        asyncio.link(sendQueue, sender, receiver, monitor)
        tg.create_task(worker(receiveQueue, sendQueue, coroutineCount-1))
        print("started")
    print("finished")
           
def init(number: int):
    writeSpecification(number)
    asyncio.run(main(number))

# asyncio.run(init(10))

runner = pyperf.Runner()
runner.bench_func('Bencmark 10000', init(100))