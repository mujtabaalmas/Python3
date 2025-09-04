import time
import asyncio
import aiohttp
import requests

async def main():
    sites = [
        "https://soundcloud.com/",
        #"http://olympus.realpython.org/dice",
        "https://ucp.edu.pk/"
        #"https://www.youtube.com/"
    ] * 20  # many downloads
    start_time = time.perf_counter()
    await download_all_sites(sites)
    duration = time.perf_counter() - start_time
    print(f"Read {len(sites)} sites in {duration:.2f} seconds")

async def download_all_sites(sites):
     async with aiohttp.ClientSession() as session:
        tasks = [download_site(url, session) for url in sites]
        await asyncio.gather(*tasks, return_exceptions=True)

async def download_site(url, session):
  async with session.get(url) as response:
        cooontent = await response.read()
        print(f"Read {len(cooontent)} bytes from {url}", flush= True)
        
        # Clean filename for safety
        filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
        #filename = f"{filename}_{index}   #.txt  # Add index to make each file unique

        with open(filename, "wb") as dfile:
            dfile.write(cooontent)


asyncio.run(main())
