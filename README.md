# YVR Hot Chocolate Festival Search
Vancouver, BC has an annual hot chocolate festival with numerous vendors. As of 2023 there is no search on the website. This program allows a user to search for a specific keyword, e.g. "white chocolate", "cinnamon", etc. Each vendor's page has a list of their available flavours. The program returns a link to each vendor's page if the keyword appears on that page. 

This program was written with Python. It uses Selenium and BeautifulSoup. 

## How to use
To populate or update the csv file, run scrape.py. To search for a keyword, run main.py. 

## To Do
- [x] Gather the href of all vendors into a list - use BeautifulSoup
- [x] Clean data - not consistently listed, ensure the links are complete
- [x] Remove duplicates in list
- [x] Open each page and search if keyword exists, if it does return link to that page
- [x] Make keyword search input value and not hardcoded
- [x] Make the keyword search case insensitive
- [x] Make scrape.py to scrape website and then write content into a csv file
- [x] Main.py searches for entered keyword in the csv file and return the link to the vendor page
