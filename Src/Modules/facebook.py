from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep
import json
import os
import re
from googletrans import Translator

def scrape_facebook_marketplace(should_stop, ui_callback, Get_category):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CHROME_PATH = os.path.join(BASE_DIR, "..", "..", "ChromeDriver", "chromedriver.exe")

    service = Service(CHROME_PATH)
    driver = webdriver.Chrome(service=service)
    url = f"https://www.facebook.com/marketplace/108132892547596/search?query={Get_category}"
    driver.get(url)

    # Load cookies
    SRC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    COOKIES_PATH = os.path.join(SRC_DIR, "Settings", "cookies.json")

    with open(COOKIES_PATH, "r") as file:
        cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

    sleep(0.2)
    driver.refresh()
    sleep(1)

    seen_listings = set()
    scroll_pause = 1.5

    while not should_stop():
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        listings = soup.find_all(
            "div",
            class_="x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x135b78x x11lfxj5 x1iorvi4 xjkvuk6 xnpuxes x1cjf5ee x17dddeq"
        )

        for listing in listings:
            if should_stop():
                break

            listing_id = str(listing)
            if listing_id in seen_listings:
                continue
            seen_listings.add(listing_id)

            try:
                # PRICE
                price_span = listing.find(
                    "span",
                    class_="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u"
                )
                price = None
                if price_span:
                    price_text = price_span.find(text=True, recursive=False)
                    if price_text:
                        cleaned_price = re.sub(r'[^0-9,]', '', price_text)
                        price = cleaned_price if cleaned_price else "Free"

                # TITLE
                title_span = listing.find(
                    "span",
                    class_="x1lliihq x6ikm8r x10wlt62 x1n2onr6"
                )
                title = title_span.find(text=True, recursive=False) if title_span else None

                # Skip listing if no title or price
                if not title or not price:
                    continue

                # TRANSLATE TITLE
                try:
                    translator = Translator()
                    translated = translator.translate(title, src='he', dest='en').text
                except Exception as e:
                    print("Translation failed:", e)
                    translated = title

                # CITY / LOCATION
                city_span = listing.find(
                    "span",
                    class_="x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1j85h84"
                )
                city = re.sub('[a-zA-Z,]', '', city_span.text) if city_span else "Unknown"

                location_a = listing.find(
                    "a",
                    "x1i10hfl xjbqb8w x1ejq31n x18oe1m7 x1sy0etr xstzfhl x972fbf x10w94by x1qhh985 x14e42zd x9f619 x1ypdohk xt0psk2 x3ct3a4 xdj266r x14z9mp xat24cr x1lziwak xexx8yu xyri2b x18d9i69 x1c1uobl x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xkrqix3 x1sur9pj x1s688f x1lku1pv"
                )
                full_url = "https://facebook.com" + location_a.get("href") if location_a else "N/A"

                # CALLBACK / OUTPUT
                print(f"Found listing: {translated}\nPrice: {price}\nCity: {city}\nURL: {full_url}\n")
                ui_callback(translated, price, full_url, city)

            except Exception as e:
                print("Error processing listing:", e)
                continue

        # Scroll page
        driver.execute_script("window.scrollBy(0, 1000);")
        sleep(scroll_pause)

    driver.quit()
    print("Scraper stopped cleanly.")
