import asyncio
import random
import src.core.instrumentation as inst
from src.core.instrumentation import Channel
from src.core.monitor import Monitor

customer = "customer"
agency = "agency"
service = "service"
specification_path = r".\travelAgency.txt"
monitor = Monitor(specification_path)

customer_to_agency = Channel(customer, agency, monitor, 1)
agency_to_customer = Channel(agency, customer, monitor, 1)
agency_to_service = Channel(agency, service, monitor, 1)
customer_to_service = Channel(customer, service, monitor, 1)
service_to_customer = Channel(service, customer, monitor, 1)

destinations = ["Aruba", "Bonaire", "Germany", "Belgium", "Norway"]
prices = {"Aruba": 3000, "Bonaire":3200, "Germany":800, "Belgium":500, "Norway":1500}

async def customer():
    going = False
    counter = 0
    while not going and counter < 6:
        destination = random.choice(destinations)
        print(f"Customer wilt naar {destination}")
        await customer_to_agency.send(destination)
        price = await agency_to_customer.receive()
        counter += 1
        if price <= 500:
            print(f"{str(price)} is een mooie prijs")
            going = True
            await customer_to_agency.send(True)
            await customer_to_service.send("Adres")
            date = await service_to_customer.receive()
            print(f"Ticket dispatch date is {date}")
    if not going:
        print(f"Deze agency heeft geen goede prijzen!")
        await customer_to_agency.send(False)

async def agency():
    loop_guard = True
    destination = await customer_to_agency.receive()
    while loop_guard:
        price = prices.get(destination)
        await agency_to_customer.send(price)
        await agency_to_service.send(destination)
        bool_or_str = await customer_to_agency.receive()
        if type(bool_or_str) == bool:
            loop_guard = False
            if bool_or_str:
                await agency_to_service.send(True)
            else:
                await agency_to_service.send(False)
        else:
            destination = bool_or_str
  

async def service():
    loop_guard = True
    destination = await agency_to_service.receive()
    while loop_guard:
        bool_or_string = await agency_to_service.receive()
        if type(bool_or_string) == bool:
            loop_guard = False
            if bool_or_string:
                adres = await customer_to_service.receive()            
                await service_to_customer.send("1 april")
        else:
            destination = bool_or_string

async def main():
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(customer())
        task_group.create_task(agency())
        task_group.create_task(service())

asyncio.run(main())
