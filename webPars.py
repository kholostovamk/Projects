"""
This has to be installed for working order:
pip install beautifulsoup4 -  library that makes it easy to scrape information from web pages
pip install requests
pip install pandas


"""

#import libraries
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#request
URL_Template = "http://books.toscrape.com/?" 
request1 = requests.get(URL_Template)
print(request1.status_code)

print(request1.text)

#want to find out books names

soup = bs(request1.text, "html.parser")

#find all article elements with the class 'product_pod'
articles = soup.find_all('article', class_ = 'product_pod')

for article in articles:
   book_title =  article.img['alt']
   print(book_title)
