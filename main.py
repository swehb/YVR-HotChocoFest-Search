import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


keyword = str(input("What flavour are you looking for? "))

URL = "https://hotchocolatefest.com/list-of-flavours"
raw_vendors = []
all_vendors = []
vendor_page = requests.get(URL)
soup = BeautifulSoup(vendor_page.content, "html.parser")


# Finds all vendor href links and adds to a list
for link in soup.find_all("a", class_="x-el x-el-a c1-1 c1-21 c1-22 c1-1a c1-1b c1-2s c1-23 c1-7l c1-b c1-2d c1-1i "
                                      "c1-29 c1-2a c1-2b c1-2c"):
    find_href = link.get("href")
    raw_vendors.append(find_href)


# Cleans the data gathered in previous step
for item in raw_vendors:
    if item.startswith("/"):
        all_vendors.append("https://hotchocolatefest.com"+item)
    elif item.startswith("http"):
        all_vendors.append(item)
    else:
        continue


# Removes duplicates
all_vendors = list(dict.fromkeys(all_vendors))


# Uses Selenium to open each vendor's page and search for the keyword
for link in all_vendors:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'),
                              options=chrome_options)
    driver.get(link)
    get_source = driver.page_source
    search_text = keyword
    if search_text in get_source:
        print(link)
    time.sleep(2)
