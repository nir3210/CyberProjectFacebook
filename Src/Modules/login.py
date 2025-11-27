import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Init
service = Service(executable_path="..\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://facebook.com/marketplace")

input("Please Press Enter After You Log in, So The program can save the cookies")


cookies = driver.get_cookies()
with open("cookies.json", 'w') as file:
    json.dump(cookies,file , indent=4)
