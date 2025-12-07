import sys
sys.dont_write_bytecode = True

import cloudscraper
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep
import json


def parse(text: str, left: str, right: str) -> str:
    start = text.index(left) + len(left)
    end = text.index(right, start)
    return text[start:end]


def scrape_amazon():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CHROME_PATH = os.path.join(BASE_DIR, "..", "..", "ChromeDriver", "chromedriver.exe")
    service = Service(CHROME_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get("https://amazon.com")
    sleep(2)
    #open the prefrence page, gotta change the NIS->USD
    driver.get("https://www.amazon.com/customer-preferences/edit/")
    sleep(2)

    wait = WebDriverWait(driver, 10) # max 10 seconds before Quiting!

    dropdown = wait.until(EC.element_to_be_clickable(
        (By.ID, "icp-currency-dropdown-selected-item-prompt")
    ))
    dropdown.click()

    usd_option = wait.until(EC.element_to_be_clickable(
        (By.ID, "icp-currency-dropdown_1")  # USD
    ))
    usd_option.click()

    save_button = wait.until(EC.element_to_be_clickable(
        (By.ID, "icp-save-button")
    ))
    save_button.click()



    # STEP 5 — Now perform search
    Search = input("enter what you would wish to search: ")
    search_url = f"https://www.amazon.com/s?k={Search.replace(' ', '+')}"
    driver.get(search_url)

    print("Search loaded successfully in USD mode.")
    sleep(100)


def get_average_price(Id: str) -> int:
    scraper = cloudscraper.create_scraper()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0"
    }

    url = f"https://camelcamelcamel.com/product/{Id}"
    print(f"URL: {url}")

    response = scraper.get(url, headers=headers)
    print("Status Code:", response.status_code)

    html = BeautifulSoup(response.text, 'html.parser')
    parent_prices = html.find(class_="pt amazon on")

    all_prices = parent_prices.find_all('td')

    prices_arr = [p.text.strip() for p in all_prices]

    print("Average USD Price:", prices_arr[4])
    return prices_arr[4]


def main():
    scrape_amazon()


if __name__ == "__main__":
    main()
