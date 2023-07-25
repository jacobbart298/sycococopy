"""
This code fragment is related to the Travel Agency Multiparty Session example
in chapter 1 in A Very Gentle Introduction to Multiparty Session Types.

Global type for the communication between Customer, Agency and Hotel

Customer -> Agency: details(str)
.Agency -> Hotel: details(str)
.Hotel -> Customer: ok(bool)
.end

Local type for Customer

Agency!details(str)
.Hotel?ok(bool)
.end

Local type for Agency

Customer?details(str)
.Hotel!details(str)
.end

Local type for Hotel

Agency?details(str)
.Customer!ok(bool
.end

Let us now translate these local types into python pseudocode.

Customer:

    await channel_customer_to_agency.put('details')
    confirmation = await channel_hotel_to_costumer.get()
            
Agency:

    details = await channel_customer_to_agency.get()
    await channel_agency_to_hotel.put(details)
        
Hotel:

    details = await channel_agency_to_hotel.get()
    await channel_hotel_to_costumer.put(True)

Variables:

    details:str
    booking_ok:bool


What follows is an implementation of a session that 
complies with the Costumer/Agency/Hotel protocol

"""

import asyncio 

# define the communication channels
channel_customer_to_agency = asyncio.Queue()
channel_agency_to_hotel = asyncio.Queue()
channel_hotel_to_costumer = asyncio.Queue()

# set a constant for sleep time
DELAY = 0.1

async def Customer():
    # generating details
    await asyncio.sleep(DELAY)
    details = 'details'
    print(f'The customer is providing the following details: {details}')
    # send details to the agency
    await channel_customer_to_agency.put('details')
    # await confirmation from the hotel
    booking_ok = await channel_hotel_to_costumer.get()
    print(f'Is the booking ok? {booking_ok}')

async def Agency():
    # await details from the customer
    details = await channel_customer_to_agency.get()
    # forward details to the hotel
    await channel_agency_to_hotel.put(details)
    print(f"The agency has forwarded the customer's details to the hotel")

async def Hotel():
    # await details from the agency
    details = await channel_agency_to_hotel.get()
    # process the booking
    await asyncio.sleep(DELAY)
    booking_ok = True
    print(f"The hotel has created a new booking: {details}")
    # confirm the booking to the customer
    await channel_hotel_to_costumer.put(booking_ok)

async def main():
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(Customer())
        task_group.create_task(Agency())
        task_group.create_task(Hotel())

asyncio.run(main())