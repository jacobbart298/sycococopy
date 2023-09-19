import asyncio
import trio
from asyncio import Queue

async def greenProducer(queue: Queue):
    while True:
        await asyncio.sleep(0.3)
        await queue.put('groen')
    
async def redProducer(queue: Queue):
    while True:
        await asyncio.sleep(0.5)
        await queue.put('rood')

async def consumer():
    queue1: Queue = Queue(maxsize=1)
    queue2: Queue = Queue(maxsize=1)

    taskGreen = asyncio.create_task(greenProducer(queue1))
    print(f'{taskGreen} has started')
    taskRed = asyncio.create_task(redProducer(queue2))
    print(f'{taskRed} has started')

    while True:
        color1 = await queue1.get()
        print(f"Van de groene producer kreeg ik {color1}")
        color2 = await queue2.get()
        print(f"Van de rode producer kreeg ik {color2}")

asyncio.run(consumer())