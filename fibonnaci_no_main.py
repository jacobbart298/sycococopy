import asyncio

async def alice(limit: int) -> int:
    x = 0
    y = 1
    while y < limit:
        next = x + y
        x = y
        y = next
        await bob(next)
    return x + y

async def bob(x: int) -> bool:
    if x % 3 == 0:
        print(f'{x} is een fibonacci getal deelbaar door 3')
    return True

asyncio.run(alice(1000000))