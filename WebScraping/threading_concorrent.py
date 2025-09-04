import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests

thread_local = threading.local()

def main():
    sites = [
        "https://www.chatgpt.com/",
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.perf_counter()
    download_all_sites(sites)
    duration = time.perf_counter() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")

def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=60) as executor:
        executor.map(download_site, sites)

def download_site(url):
    session = get_session_for_thread()
    with session.get(url) as response:
        print(f"Read {len(response.content)} bytes from {url}")
        filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
        #filename = f"{filename}_{index}   #.txt  # Add index to make each file unique
        with open(filename, "wb") as dfile:
            dfile.write(response.content)

def get_session_for_thread():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

if __name__ == "__main__":
    main()