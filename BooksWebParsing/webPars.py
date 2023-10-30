"""
This has to be installed for working order:
pip install beautifulsoup4 -  library that makes it easy to scrape information from web pages
pip install requests
pip install pandas


"""

#required libraries for web scraping and data handling
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#function to fetch anf parse HTML from the provided URL
def get_soup_from_url(url):
    response = requests.get(url)
    #raise an error if the request is not successful
    if response.status_code !=200:
        raise ValueError(f'Failed to retrieve the webpage. Status code: {response.status_code}')
    #parse fetched HYML and return parsed object
    return bs(response.text, "html.parser")

#function to retract book details from the a given article tag
def get_book_details(article):
    title = article.img['alt']
    price_tag = article.find('p', class_='price_color')
    price = price_tag.text if price_tag else None# actual rating, not stars
    rating = article.find('p', class_='star-rating')['class'][1]
    availability = article.find('p', class_="instock availability").text.strip()

    #return extracted details in the form of dictionary
    return {
        'Title': title,
        'Price': price,
        'Rating': rating,
        'Availability': availability
    }

def main():
    
    URL_Template = "http://books.toscrape.com/?"
    filename = 'books.csv'

    #fetch and parse URL from chosen URL
    soup = get_soup_from_url(URL_Template)
    
    articles = soup.find_all('article', class_='product_pod')
    #extract details of each book
    books = [get_book_details(article) for article in articles]

    #convert list of dictionaries into dataframe
    df = pd.DataFrame(books)
    #convert dataframe to csv file
    df.to_csv(filename, index=False)

## Ensure the script is being run as a standalone file, not imported as a module
if __name__ == "__main__":
    main()