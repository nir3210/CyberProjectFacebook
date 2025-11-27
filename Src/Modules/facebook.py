from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep
import json

def scrape_facebook_marketplace():
    service = Service(executable_path="..\\..\\ChromeDriver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://facebook.com/marketplace")

    with open("cookies.json", 'r') as file:  # facebook LITERALLY forces u to log in.
        cookies = json.load(file) 
        for cookie in cookies:
            driver.add_cookie(cookie)

    sleep(2)
    driver.refresh()
    sleep(3)

    seen_listings = set() #using set because if something already is inside , it's not going to add it again
    scroll_pause = 2

    while True:
        # Scraping the html , and then getting all listings , because facebook is extremely dumb it needs to be inside the fucking while loop
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        listings = soup.find_all('div', class_='x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x135b78x x11lfxj5 x1iorvi4 xjkvuk6 xnpuxes x1cjf5ee x17dddeq')
        
        
        #this for loop is used because we need to identify if its a dupe or not, we don't want to have the same thing twice.
        for listing in listings:
            listing_id = str(listing)
            if listing_id in seen_listings:
                continue

            seen_listings.add(listing_id) # adding to the set so we can avoid for next times
            

            try:     
                price_span = listing.find('span', class_='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u')
                if price_span:
                    original_proce = price_span.find(text=True, recursive=False) # recursive is default on , but we want only the first value becuase it has 2 values if its on discount and then giving an err : 450 nis 500 nis ...
                    if original_proce:
                        print(original_proce.strip()) #not important but need to use as many functions from the course
                else: # Just pass, Facebook has bs stuff like sponssered and shit and we don't want that messing up our code 
                    pass
                sleep(0.1)
            except Exception as e:
                print(e)

        

        driver.execute_script("window.scrollBy(0, 1000);")  
        sleep(scroll_pause)

    driver.quit() # pointless , will be integrated in the future


def main():
    scrape_facebook_marketplace()

if __name__ == "__main__":
    main()