import sys
sys.dont_write_bytecode = True # Fuck Byte code , Python.

import cloudscraper
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def parse(text:str, left:str, right:str) -> str:
    start = text.index(left) + len(left)
    end = text.index(right , start)
    return text[start:end]



def get_average_price(Id:str) -> int:
    
    scraper = cloudscraper.create_scraper()

    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0"
    }


    item = "B0FQNB9WBD"
    url = f"https://camelcamelcamel.com/product/{Id}"
    print(f"=================================      URL    ====================================\n\t{url}")
    print(f"==================================================================================\n\n\n\n")    
    # Making the request to the camelcamelcamel api , tells average prices which we can compare later.
    response = scraper.get(url, headers=headers)
    print(f"===================================== STATUS CODE ================================\n\t\t\t\t\t{response.status_code}")
    print(f"==================================================================================")
    html = BeautifulSoup(response.text , 'html.parser')


    parent_prices = html.find(class_="pt amazon on")


    all_prices = parent_prices.find_all('td')


    prices_arr = []

    for price in all_prices:
        prices_arr.append(price)

    print(prices_arr[4].text.strip())

def main():

    try:
        url = input("Enter the url: ")
        ID = parse(url, 'dp/', '/')
    except Exception as ValueError:
        ID = parse(url, 'dp/' , '?')
    a = get_average_price(ID)
    

if __name__ == "__main__":
    main()
"""
url ref:
class="a-link-normal s-no-outline"

title:
class="a-size-medium a-spacing-none a-color-base a-text-normal"

price:
class="a-price-whole"

"""
