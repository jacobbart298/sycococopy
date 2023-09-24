import asyncio
from SynchronousChannel import SynchronousChannel

channelGreen = SynchronousChannel()
channelRed = SynchronousChannel()

async def consumer():
    while(True):
        item = await channelGreen.receive()
        print(item)
        item = await channelRed.receive()
        print(item)

async def greenProducer():
    while(True):
        await asyncio.sleep(0.5)
        await channelGreen.send("green")

async def redProducer():
    while(True):
        await asyncio.sleep(0.3)
        await channelRed.send("red")

async def main():
    await asyncio.gather(
        greenProducer(),
        redProducer(),
        consumer()
    )

asyncio.run(main())
