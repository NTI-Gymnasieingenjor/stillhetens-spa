import os
from selenium import webdriver 
import argparse
from sys import platform

if platform == "linux":
    exe=""
else:
    exe=".exe"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(executable_path=(os.getcwd() + "/../chromedriver" + exe), chrome_options=options)
driver.get("https://fantastic4group.gitlab.io/pizza-website/")

assert driver.find_element_by_id("titleTextTest") == "eeee"
print(driver.find_element_by_id("titleTextTest"))