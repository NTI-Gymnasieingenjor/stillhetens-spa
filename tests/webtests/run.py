import os
from selenium import webdriver
import argparse
from sys import platform
import subprocess
from atexit import register

from infoTest import InfoTest

# Checks if the test is run on Linux or Windows,
# and chooses driver accordingly
if platform == "linux":
    exe = ""
else:
    exe = ".exe"


# Opens a localhost server with the port 6969 and in the public directory
server = subprocess.Popen(["python3", "-m", "http.server",  "6969"],
                          cwd="../../public", stdout=open(os.devnull, "w"), stderr=open(os.devnull, "w"))

# Closes the server at the end
def exitFunction():
    server.terminate()
    print("Test Finished")

register(exitFunction)

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

driver.get("http://localhost:6969/index.html")

print("")

InfoTest(driver)