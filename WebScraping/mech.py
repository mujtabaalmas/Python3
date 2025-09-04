import mechanicalsoup
import time 
import datetime

browser = mechanicalsoup.Browser()
for i in range(5):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.next
    tag = page.soup.select("#time")[0]
    start_time = datetime.datetime.now(datetime.UTC)
    print(f"The result of your dice roll is: {result}")
    print(f"Time: {start_time}")
    if i<5:
        time.sleep(0)