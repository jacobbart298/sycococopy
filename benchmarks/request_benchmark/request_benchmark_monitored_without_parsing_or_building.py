import aiohttp
import pyperf
import src.core.instrumentation as asyncio
from src.core.monitor import Monitor

'''
Benchmark to test the compare the framework in a real world scenario where website requests are
handled and results passed between coroutines. 
Benchmark with monitoring including full parsing
'''

URLS = 2
specification = 'requests.txt'

async def getResponse(incoming, outgoing):
    i = 0
    while i < URLS:
        url = await incoming.get()
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                status = response.status
                await outgoing.put(status)
                header = response.headers['content-type']
                await outgoing.put(header)
        i += 1

async def handleResponse(incoming, outgoing):
    status_codes = []
    headers = []
    urls = ['http://python.org', 'http://example.com']
    i = 0
    while i < URLS:
        await outgoing.put(urls[i])
        status = await incoming.get()
        header = await incoming.get()
        status_codes.append(status)
        headers.append(header)
        i += 1

async def main():
    monitor.fsm.states = {initialState}
    handle_to_response = asyncio.Queue()
    response_to_handle = asyncio.Queue()
    asyncio.link(handle_to_response, "handler", "requester", monitor)
    asyncio.link(response_to_handle, "requester", "handler", monitor)
    await asyncio.gather(getResponse(handle_to_response, response_to_handle), handleResponse(response_to_handle, handle_to_response))

if __name__ == '__main__':
    monitor = Monitor(specification)
    initialState = list(monitor.fsm.states)[0]
    runner = pyperf.Runner()
    runner.bench_async_func(f"Request", main)