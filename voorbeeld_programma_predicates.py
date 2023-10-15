import src.core.instrumentation as asyncio
from src.core.instrumentation import Channel
from src.core.monitor import Monitor

A = 'A'
B = 'B'
C = 'C'

specification_path = r".\protocol_voorbeeld_programma_predicates.txt"
monitor = Monitor(specification_path)

aToB = Channel(A, B, monitor)
bToA = Channel(B, A, monitor)
bToC = Channel(B, C, monitor)

async def A():
    answer = await bToA.receive()
    if (answer):
        await aToB.send(6)
    else:
        await aToB.send(-2)

async def B():
    await bToA.send(True)
    number = await aToB.receive()
    await bToC.send(f"Number received: {number}")

async def C():
    number_string = await bToC.receive()
    print(number_string)

async def main():
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(A())
        task_group.create_task(B())
        task_group.create_task(C())

asyncio.run(main())