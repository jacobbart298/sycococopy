from src.auto import Auto
from src.core.instrumentation import Channel
import src.core.instrumentation as asyncio
from src.core.monitor import Monitor

buyer1 = "buyer1"
buyer2 = "buyer2"
seller = "seller"
specification_path = "protocol_voorbeeld_programma_reference_types.txt"
monitor = Monitor(specification_path)

buy1tobuy2 = Channel(buyer1, buyer2, monitor)
buy2tobuy1 = Channel(buyer2, buyer1, monitor)
buy1tosell = Channel(buyer1, seller, monitor)
buy2tosell = Channel(buyer2, seller, monitor)
selltobuy1 = Channel(seller, buyer1, monitor)
selltobuy2 = Channel(seller, buyer2, monitor)
 
async def buyer1():
    await buy1tosell.send(Auto("Tesla", 3000))
    await buy1tosell.send(Auto("Mercedes", 348734))
    quote = await selltobuy1.receive()
    await buy1tobuy2.send(quote//2)
    buys_book = await buy2tobuy1.receive()
    if buys_book:
        await buy1tobuy2.send(quote//2)

async def buyer2():
    cost = await selltobuy2.receive()
    buyer1Contributes = await buy1tobuy2.receive()
    if cost-buyer1Contributes >= 20:
        await buy2tobuy1.send(True)
        await buy1tobuy2.receive()
        await buy2tosell.send(cost)
    else:
        await buy2tobuy1.send(False)
        await buy2tosell.send(False)

async def seller():
    auto1 = await buy1tosell.receive()
    auto2 = await buy1tosell.receive()
    print(f"Auto1 is een {auto1.merk} en heeft kmstand {auto1.kilometerstand}")
    print(f"Auto2 is een {auto2.merk} en heeft kmstand {auto2.kilometerstand}")
    await selltobuy1.send(60)
    await selltobuy2.send(60)
    await buy2tosell.receive()

async def main():
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(buyer1())
        task_group.create_task(buyer2())
        task_group.create_task(seller())

asyncio.run(main())
