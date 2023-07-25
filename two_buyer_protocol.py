"""
This code fragment is related to the Two Buyer Protocol
in paragraph 2.3 in Multiparty Asynchronous Session Types.

Global type for the communication between Buyer1, Buyer2 and Seller

Buyer1 -> Seller: title(str)
.Seller -> Buyer1: quote(int)
.Seller -> Buyer2: quote(int)
.Buyer1 -> Buyer2: contribution(int)
.Buyer2 -> Seller: {accept(bool).end.,
                    reject(bool).end} 

Note that it does not matter in which order the quotes from 
Seller to Buyer1 and Buyer2 are sent. This info is not yet
explicated in the global type nor in the local type.

Local type for Buyer1

Seller!title(str)
.Seller?quote(int)
.Buyer2!contribution(int)
.end)

Local type for Buyer2

Seller?quote(int)
.Buyer1?contribution(int)
.if (contribution > quote/2)
 then Seller!accept(bool).end
 else Seller!reject(bool).end

Local type for Seller

Buyer1?title(str)
.Buyer1!quote(int)
.Buyer2!quote(int)
.((Buyer2?accept(bool).end) + (Buyer2?reject(bool).end))

Let us now translate these local types into python pseudocode.

Buyer1:

    await channel_buyer1_seller.put(title)
    quote = await channel_seller_buyer1.get()
    await channel_buyer1_buyer2.put(contribution)
            
Buyer2:

    quote = await channel_seller_buyer2.get()
    contribution = await channel_buyer1_buyer2.get()
    await channel_buyer2_seller.put(contribution >= quote/2)
        
Seller:

    title = await channel_buyer1_seller.get()
    await channel_seller_buyer1.put(quote)
    await channel_seller_buyer2.put(quote)
    to_buy = await channel_buyer2_seller.get()

Variables:

    title:str
    quote:int
    contribution:int
    to_buy:bool
    
What follows is an implementation of a session that 
complies with the Two Buyer Protocol.

"""

import asyncio
import random

# define the communication channels
channel_buyer1_seller = asyncio.Queue()
channel_buyer1_buyer2 = asyncio.Queue()
channel_buyer2_seller = asyncio.Queue()
channel_seller_buyer1 = asyncio.Queue()
channel_seller_buyer2 = asyncio.Queue()

# define the book catalogue
book_price_dictionary = {"The Infatuations" : 9,
                         "All Souls" : 8,
                         "Tomorrow in the Battle Think on Me" : 7,
                         "Tomas Nevinson" : 20}

# set a constant for sleep time
DELAY = 0.1

async def buyer1():
    # determine a book of interest
    await asyncio.sleep(DELAY)
    title = random.choice(list(book_price_dictionary.keys()))
    print(f"Buyer1 has chosen {title}")
    # send book title to seller
    await channel_buyer1_seller.put(title)
    # await the quote from seller
    quote = await channel_seller_buyer1.get()
    # determine the amount to contribute
    await asyncio.sleep(DELAY)
    contribution = random.randint(0, quote)
    print(f"Buyer1 is willing to contribute {contribution} euros")
    # send the contribution to buyer2
    await channel_buyer1_buyer2.put(contribution)

async def buyer2():
    # await the quote from seller
    quote = await channel_seller_buyer2.get()
    # await the contribution from buyer1
    contribution = await channel_buyer1_buyer2.get()
    # determine whether or not to buy the book
    await asyncio.sleep(DELAY)
    to_buy = contribution >= quote/2
    print(f"Does buyer2 decide to buy the book? {to_buy}")
    # notify the seller of the decision
    await channel_buyer2_seller.put(to_buy)

async def seller():
    # await the book title from buyer1
    title = await channel_buyer1_seller.get()
    # determine the quote of the book
    await asyncio.sleep(DELAY)
    quote = book_price_dictionary.get(title)
    print(f"The quote for {title} is {quote} euros")
    # send the quote to buyer1
    await channel_seller_buyer1.put(quote)
    # send the quote to buyer2
    await channel_seller_buyer2.put(quote)
    # await buyer2's decision whether or not to buy
    to_buy = await channel_buyer2_seller.get()
    print (f"Has the deal closed? {to_buy}")

async def main():
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(buyer1())
        task_group.create_task(buyer2())
        task_group.create_task(seller())

asyncio.run(main())