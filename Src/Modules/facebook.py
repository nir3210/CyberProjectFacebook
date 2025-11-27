# I DONT WANT FUCKING PYC FILES!!
import sys
sys.dont_write_bytecode = False

import os
print("[DEBUG]: Driver Path Exists:", os.path.exists("..\\..\\ChromeDriver\\chromedriver.exe"))

# selenium , so many fucking imports.  


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


from time import sleep
import json

#Start App
service = Service(executable_path="..\\..\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://facebook.com/marketplace")

with open("cookies.json", 'r') as file:
    cookies = json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)


driver.refresh()
sleep(10)

driver.quit()