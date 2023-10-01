import asyncio
import src.core.instrumentation as inst
from src.core.instrumentation import Channel
from src.core.monitor import Monitor

buyer1 = "buyer1"
buyer2 = "buyer2"
seller = "seller"
specification_path = ".\protocol_voorbeeld_programma.txt"
monitor = Monitor(specification_path)

buy1tobuy2 = Channel(buyer1, buyer2, monitor, 1)
buy2tobuy1 = Channel(buyer2, buyer1, monitor, 1)
buy1tosell = Channel(buyer1, seller, monitor, 1)
buy2tosell = Channel(buyer2, seller, monitor, 1)
selltobuy1 = Channel(seller, buyer1, monitor, 1)
selltobuy2 = Channel(seller, buyer2, monitor, 1)
 
async def buyer1():
    await buy1tosell.send("A Rumor of War")
    quote = await selltobuy1.receive()
    await buy1tobuy2.send(quote//2)
    buys_book = await buy2tobuy1.receive()
    print(f"Buyer1 finished, buys_book = {buys_book}")

async def buyer2():
    cost = await selltobuy2.receive()
    buyer1Contributes = await buy1tobuy2.receive()
    if cost-buyer1Contributes <= 20:
        await buy2tobuy1.send(True)
        await buy2tosell.send(cost)
    else:
        await buy2tosell.send(False)
        await buy2tobuy1.send(False)
    print("Buyer 2 finished")

async def seller():
    await buy1tosell.receive()
    await selltobuy1.send(60)
    await selltobuy2.send(60)
    response = await buy2tosell.receive()
    if response:
        print(f"Seller sold book for {response} Euro")
    else:
        print("Seller ended, no deal made")

async def main():
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(buyer1())
        task_group.create_task(buyer2())
        task_group.create_task(seller())

asyncio.run(main())
