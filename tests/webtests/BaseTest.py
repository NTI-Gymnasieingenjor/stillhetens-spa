import os
from selenium import webdriver 
import argparse
from sys import platform

if platform == "linux":
    exe=""
else:
    exe=".exe"

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(executable_path=(os.getcwd() + "/../chromedriver" + exe), chrome_options=options)