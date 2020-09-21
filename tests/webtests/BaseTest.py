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
driver = webdriver.Chrome(executable_path=(os.getcwd() + "/../chromedriver" + exe), options=options)
driver.get("google.com")

assert driver.find_element_by_id("hplogo")