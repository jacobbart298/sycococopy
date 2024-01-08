import aiohttp
import pyperf
import asyncio
from requests.exceptions import HTTPError

URLS = 2

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
    # print(f"The received status codes were {status_codes}")
    # print(f"The received headers were {headers}")

async def main():
    handle_to_response = asyncio.Queue()
    response_to_handle = asyncio.Queue()
    await asyncio.gather(getResponse(handle_to_response, response_to_handle), handleResponse(response_to_handle, handle_to_response))

if __name__ == '__main__':
    runner = pyperf.Runner()
    runner.bench_async_func(f"Request", main)

