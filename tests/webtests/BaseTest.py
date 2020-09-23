import os
from selenium import webdriver 
import argparse
from sys import platform

# Checks if the test is run on Linux or Windows
if platform == "linux":
    exe=""
else:
    exe=".exe"

# Creates the variable for ChromeOptions()
options = webdriver.ChromeOptions()
# Makes the test run in the terminal instead of the browser
options.add_argument("--headless")
# Gives Chrome access to the rest of the system 
options.add_argument("--no-sandbox")
# Writes shared memory files into /tmp instead of /dev/shm
options.add_argument("--disable-dev-shm-usage")
# Gets the driver and defines its options
driver = webdriver.Chrome(executable_path=(os.getcwd() + "/../chromedriver" + exe), chrome_options=options)