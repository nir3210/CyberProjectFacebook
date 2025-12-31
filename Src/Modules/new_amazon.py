import sys
sys.dont_write_bytecode = True
import os
import json
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, init
init(autoreset=True)


# debug just for easier printing
def debug(message:str, mode=0) -> None:
    if mode == 1: # just for looks , nothing else!
        phrased_message = f"[{Fore.LIGHTCYAN_EX}*{Fore.RESET}]: {message}"
    else:
        phrased_message = f"[{Fore.GREEN}DEBUG{Fore.RESET}]: {message}"
    print(phrased_message)

# basically just init the driver and get it ready , will be implemented new features in the future e.g: diff drivers auto install chromedriver etc.  
def initDriver() -> webdriver.Chrome:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # i got to use absolute path , python works weirdly with the defs and calling functions from other files , i want to avoid that mess 
    CHROME_PATH = os.path.join(BASE_DIR, "..", "..","ChromeDriver", "chromedriver.exe") 
    service = Service(CHROME_PATH)
    driver = webdriver.Chrome(service=service)
    if driver:
        debug("initialized driver", 1)
        return driver # gotta return it , duh.

# this function mainly exists because we use camelcamelcamel api , its working with usd so why we wouldn't?
"""
NORMALLY THIS FUNCTION SHOULD NOT EXIST!
we can just change the url paramaters but i do it because it takes ~5 secs and it saves the hustle from bypassing the captcha - never did i ever get a captcha test with this method
"""
def set_currency_nis_to_usd(driver: webdriver.Chrome) -> None:
    driver.get("https://amazon.com") # i found it effective against the captcha for amazon that if i sleep for 2 seconds and then refer it to the actual settings , it just doesn't notice it. gotta prob be something with cookies
    sleep(2) 
    driver.get("https://www.amazon.com/customer-preferences/edit") # actual url for settings
    wait = WebDriverWait(driver,10); # wait a max of 10 seconds! we don't want more than that!


    # https://stackoverflow.com/questions/59130200/selenium-wait-until-element-is-present-visible-and-interactable - helped a ton.
    dropdown = wait.until(EC.element_to_be_clickable
        (
            (By.ID, "icp-currency-dropdown-selected-item-prompt") # for the dropdown menu, gotta click it 
        )
    )
    dropdown.click()
    usd = wait.until(
        EC.element_to_be_clickable
        (
            (By.ID , "icp-currency-dropdown_1") # usd id
        )
    )
    usd.click()
    save = wait.until(
        EC.element_to_be_clickable
        (
            (By.ID, "icp-save-button") # save settings
        )
    )
    save.click()
    if save:
        debug("Changed nis to usd", 1)

def searchAmazon(driver: webdriver.Chrome , query):
    sleep(1) # just so it doesn't do any bugs , safe to say this is obligatory.
    search = driver.find_element(By.ID, "twotabsearchtextbox") 
    search.send_keys(query)
    search.send_keys(Keys.ENTER)
    debug(query)



def scrape_listings(soup):
    listings = soup.find_all('div', {'data-asin': True})  # more generic, catches all products  - every amazon product has it
    debug(f"Found {len(listings)} listings")
    
    for listing in listings:
        title_h2 = listing.find('h2', class_="a-size-medium a-spacing-none a-color-base a-text-normal")
        price_span = listing.find('span', class_='a-price-whole')
        
        if title_h2 and price_span:
            title = title_h2.get_text().strip()
            price = price_span.contents[0].strip()
            debug(f"Title: {title} | Price: {price}$" , 1)
        else:
            continue



def go_to_next_page(driver, soup) -> bool:
    try:
        next_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.s-pagination-next"))
        )

        next_btn.click()

        # wait for products on the next page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-asin]"))
        )
        wait = WebDriverWait(driver, 10) # max 10 seconds before Quiting!
        next_button_selector = ".s-pagination-next"  
        next_page_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, next_button_selector))) # search for the element , and wait for it to be avaliable
        string_page_btn = soup.select(next_button_selector)
        
        if "s-pagination-disabled" in str(string_page_btn):
            print(f"[DEBUG]: no more pages to scrape, exiting!")
            sleep(100)
            driver.quit()
            exit()
            return False
        return True

    except:
        return False

def main() -> None:
    driver = initDriver()
    set_currency_nis_to_usd(driver)

    searchAmazon(driver, "cpu cooler")
    html = driver.page_source 
    soup = BeautifulSoup(html, 'html.parser')
    while True:
            soup = BeautifulSoup(driver.page_source, "html.parser")
            scrape_listings(soup)
            next_page = go_to_next_page(driver, soup)

            if not next_page:
                break # no more pages

if __name__ == "__main__":
    main()
    sleep(100)


"""
def get_arrays_as_list():
    array1 = [1, 2, 3]
    array2 = [4, 5, 6]
    return [array1, array2]

"""


