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

import pprint

#request
URL_Template = "http://books.toscrape.com/?" 
request1 = requests.get(URL_Template)
#print(request1.status_code)

#print(request1.text)

#want to find out books names

soup = bs(request1.text, "html.parser")

#find all article elements with the class 'product_pod'
articles = soup.find_all('article', class_ = 'product_pod')

print(len(articles))

#dictionary to store books info
books_dict = {}

for article in articles:
   title =  article.img['alt']
   price_tag = article.find('p', class_ = 'price_color')
   price = price_tag.text if price_tag else None
   rating = article.find('p', class_ = 'star-rating')['class'][1] #actual rating, not stars
   availability = article.find('p', class_ = "instock availability").text.strip()
   
   #storing it in dictionary
   books_dict[title] = {
      'Price': price,
      'Rating': rating,
      'Availability': availability
    }


#printing out dictionary
for title, details in books_dict.items():
   print(f'{title}')
   for key, value in details.items():
      print(f'   {key}: {value}')