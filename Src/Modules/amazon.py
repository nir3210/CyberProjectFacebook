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
from selenium.webdriver.chrome.options import Options
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
def initDriver(debug_enabled: bool) -> webdriver.Chrome:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # absolut path
    CHROME_PATH = os.path.join(BASE_DIR, "..", "..", "ChromeDriver", "chromedriver.exe")

    service = Service(CHROME_PATH)
    options = Options()

    if not debug_enabled:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=service, options=options)
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



def scrape_listings(soup,ui_callback, results_list):
    listings = soup.find_all('div', {'data-asin': True})  # more generic, catches all products  - every amazon product has it
    debug(f"Found {len(listings)} listings")
    
    for listing in listings:
        title_h2 = listing.find('h2', class_="a-size-medium a-spacing-none a-color-base a-text-normal")
        price_span = listing.find('span', class_='a-price-whole')
        asin = listing.get("data-asin") # .get is just a method that 
        if title_h2 and price_span and asin:
            title = title_h2.get_text().strip()
            price = price_span.contents[0].strip() # in a span in beaufiul sopup its being stored in an array , we can just get the first elemenet
            debug(f"Title: {title} | Price: {price}$ | data: {asin.strip()}" , 1) 
            ui_callback(title,price, f"https://amazon.com/dp/{asin}")
            results_list.append({
                "title": title,
                "price": price,
                "asin": asin,
                "url": f"https://amazon.com/dp/{asin}"
            }) # dict is just so much easier than an array , not even talking about o(1) complexety instead of o(n)
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

def save_listing(results):
        # Save everything to JSON at the end - Will need to implement scs
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RESULTS_PATH = os.path.join(BASE_DIR, "..", "..", "Results", "Amazon") # again , work with absolut path its so much better
    os.makedirs(RESULTS_PATH, exist_ok=True)
    file_path = os.path.join(RESULTS_PATH, "results.json")

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False) # ensure ascii false becuase amazon is weird , doesn't really matter although i like to add it to not cause any issues

    debug(f"Saved {len(results)} results to {file_path}")

def amazonScrape(should_stop,ui_callback, search, debug) -> None:
    driver = initDriver(debug)
    set_currency_nis_to_usd(driver)

    searchAmazon(driver, search)
    results = [] # array to store the results

    while not should_stop():
        soup = BeautifulSoup(driver.page_source, "html.parser")
        scrape_listings(soup,ui_callback, results)  # pass results list
        next_page = go_to_next_page(driver, soup)

        if not next_page:
            break # means that nothing 
    
    driver.quit()
    save_listing(results)


