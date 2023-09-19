import asyncio

async def alice(limit: int) -> int:
    x = 0
    y = 1
    while y < limit:
        next = x + y
        x = y
        y = next
        await bob(next)


async def bob(x: int) -> bool:
    if x % 3 == 0:
        print(f'{x} is een fibonacci getal deelbaar door 3')
    await eve(x)

async def eve(x:int) -> bool:
    if x % 4 == 0:
        print(f'{x} is een fibonacci getal deelbaar door 4')
    await alice(10000)

asyncio.run(alice(1000000))