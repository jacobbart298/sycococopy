import asyncio

async def alice(x: int, y: int) -> int:
    return x + y

async def bob(x: int) -> bool:
    return x % 3 == 0

async def main(limit: int) -> None:
    x = 0
    y = 1
    while y <= limit:
        next = await alice(x,y)
        x = y
        y = next
        if (await bob(y)):
            print(str(y))

asyncio.run(main(1000000))