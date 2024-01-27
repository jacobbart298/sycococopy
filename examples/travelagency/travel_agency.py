import random
import src.core.instrumentation as asyncio
from src.core.monitor import Monitor

customer = "customer"
agency = "agency"
service = "service"
specification_path = r".\travel_agency_protocol.txt"
monitor = Monitor(specification_path)

customer_to_agency = asyncio.Queue()
agency_to_customer = asyncio.Queue()
agency_to_service = asyncio.Queue()
customer_to_service = asyncio.Queue()
service_to_customer = asyncio.Queue()

asyncio.link(customer_to_agency, customer, agency, monitor)
asyncio.link(agency_to_customer, agency, customer, monitor)
asyncio.link(agency_to_service, agency, service, monitor)
asyncio.link(customer_to_service, customer, service, monitor)
asyncio.link(service_to_customer, service, customer, monitor)

destinations = ["Aruba", "Bonaire", "Germany", "Belgium", "Norway"]
prices = {"Aruba": 3000, "Bonaire":3200, "Germany":800, "Belgium":500, "Norway":1500}

async def customer():
    going = False
    counter = 0
    while not going and counter < 6:
        destination = random.choice(destinations)
        print(f"Customer wilt naar {destination}")
        await customer_to_agency.put(destination)
        price = await agency_to_customer.get()
        counter += 1
        if price <= 500:
            print(f"{str(price)} is een mooie prijs")
            going = True
            await customer_to_agency.put(True)
            await customer_to_service.put("Adres")
            date = await service_to_customer.get()
            print(f"Ticket dispatch date is {date}")
    if not going:
        print(f"Deze agency heeft geen goede prijzen!")
        await customer_to_agency.put(False)

async def agency():
    loop_guard = True
    destination = await customer_to_agency.get()
    while loop_guard:
        price = prices.get(destination)
        await agency_to_customer.put(price)
        await agency_to_service.put(destination)
        bool_or_str = await customer_to_agency.get()
        if type(bool_or_str) == bool:
            loop_guard = False
            if bool_or_str:
                await agency_to_service.put(True)
            else:
                await agency_to_service.put(False)
        else:
            destination = bool_or_str
  

async def service():
    loop_guard = True
    destination = await agency_to_service.get()
    while loop_guard:
        bool_or_string = await agency_to_service.get()
        if type(bool_or_string) == bool:
            loop_guard = False
            if bool_or_string:
                adres = await customer_to_service.get()            
                await service_to_customer.put("1 april")
        else:
            destination = bool_or_string

async def main():
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(customer())
        task_group.create_task(agency())
        task_group.create_task(service())

asyncio.run(main())
