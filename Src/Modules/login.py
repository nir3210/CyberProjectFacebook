import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os


def save_cookies():
    service = Service(executable_path="..\\ChromeDriver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://facebook.com/marketplace")



    # After the login - the program will auto save the cookies that will be used in facebook.py for auto login.
    input("Please Press Enter After You Log in, So The program can save the cookies")

    cookies = driver.get_cookies()

    SRC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    COOKIES_PATH = os.path.join(SRC_DIR, "Settings", "cookies.json")
    with open(COOKIES_PATH , 'w') as file:
        json.dump(cookies,file , indent=4)
