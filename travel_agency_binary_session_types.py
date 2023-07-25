"""
This code fragment is related to the Travel Agency Binary Session example
in chapter 1 in A Very Gentle Introduction to Multiparty Session Types.

Global type for the communication between Customer and Agency

Customer -> Agency: destination(str)
.Agency -> Customer: quote(int)
.Customer -> Agency : {
	accept(bool):
		Customer -> Agency: address(str)
		.Agency -> Customer: date(str)
		.end,
	reject(bool):end
}

Local type for Customer and Agency

Customer:

!destination(str).?quote(int).
((!accept(bool).!address(str).?date(str).end)+(!reject(bool).end))+

Agency:

?destination(str).!quote(int).
((?accept(bool).?address(str).!date(str).end)&(?reject(bool).end))

Let us rewrite each of these local types with each operation on a separate line.

Customer:

!destination(str)
.?quote(int)
.((!accept(bool)
       .!address(str)
       .?date(str)
       .end)
   +
   (!reject(bool)
       .end))
       
Agency:

?destination(str)
.!quote(int)
.((?accept(bool)
        .?address(str)
        .!date(str)
        .end)
   &
   (?reject(bool)
        .end))
        
Let us now translate these local types into python pseudocode.
    
Customer:

    await channel_customer_to_agency.put(destination)
    quote = await channel_agency_to_customer.get()
    await channel_customer_to_agency.put(proceed)
    if proceed:
        await channel_customer_to_agency.put(address)
        date = await channel_agency_to_customer.get()
        
Agency:

    destination = await channel_customer_to_agency.get()
    await channel_agency_to_customer.put(quote)
    proceed = await channel_customer_to_agency.get()
    if proceed:
        address = await channel_customer_to_agency.get()
        await channel_agency_to_customer.put(date)
        
Variables:

    destination:str
    quote:int
    proceed:bool
    address:str
    date:str  

Note the duality visible in the MPST notation, which is
reflected in the Python statements. One could say that, 
given v:type, statement await channel_b_to_a.put(v) 
has v = await channel_b_to_a.get() as its dual.

What follows is an implementation of a Costumer/Agency 
session that complies with the Costumer/Agency protocol

"""

import asyncio 
import random

# define the communication channels
channel_customer_to_agency = asyncio.Queue()
channel_agency_to_customer = asyncio.Queue()

# define the travel catalogue
destination_price_dictionary = {'Hawaii' : 5000, 'France' : 1000}

# set a constant for sleep time
DELAY = 0.1

async def Customer():
    # determine the destination
    await asyncio.sleep(DELAY)
    destination = random.choice(list(destination_price_dictionary.keys()))
    print(f'The customer has chosen {destination} as a destination')
    # send the destination to the agency
    await channel_customer_to_agency.put(destination)
    # await the quote from the agency
    quote = await channel_agency_to_customer.get()
    # determine whether or not to book
    await asyncio.sleep(DELAY)
    proceed = quote <= 1000
    print(f'Does the customer accept the quote? {proceed}')
    # notify the agency of the decision
    await channel_customer_to_agency.put(proceed)
    if proceed:
        # send the address to the agency
        await channel_customer_to_agency.put('Valkenburgerweg 177, 6419AT Heerlen, The Netherlands')
        # await the confirmation date from the agency
        date = await channel_agency_to_customer.get()
        print(f'The customer has received a confirmation for {destination} on {date}')

async def Agency():
    # await the destination from the customer
    destination = await channel_customer_to_agency.get()
    # determine the quote for the destination
    await asyncio.sleep(DELAY)
    quote = destination_price_dictionary.get(destination)
    print(f'The quote for {destination} is {quote} euros')
    # send the quote to the customer
    await channel_agency_to_customer.put(quote)
    # await the customer's decision whether or not to book
    proceed = await channel_customer_to_agency.get()
    if proceed:
        # await the customer's address
        address = await channel_customer_to_agency.get()
        # process the booking
        await asyncio.sleep(DELAY)
        print(f'The agency will send tickets to {address}')
        # send the confirmation date for the trip to the customer
        await channel_agency_to_customer.put('25-07-2023')

async def main():
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(Customer())
        task_group.create_task(Agency())

asyncio.run(main())