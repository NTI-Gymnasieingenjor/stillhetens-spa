import os
from selenium import webdriver
from sys import platform
import subprocess
from atexit import register

from infoTest import InfoTest
from socialmediaTest import SocialMediaTest
from openDaysTest import OpenDaysTest

# Checks if the test is run on Linux or Windows,
# and chooses driver accordingly
if platform == "linux":
    exe = ""
    pythonSubfix = "3"
else:
    exe = ".exe"
    pythonSubfix = ""
    
port = "6969"

# Opens a localhost server with the port 6969 in the _site directory
server = subprocess.Popen(["python" + pythonSubfix, "-m", "http.server",  port],
                          cwd="../../_site", stdout=open(os.devnull, "w"), stderr=open(os.devnull, "w"))

# Closes the server before the script finishes
def exitFunction():
    server.terminate()
    print("Test Finished")

register(exitFunction)

# Creates the variable to be able to set webdriver options
options = webdriver.ChromeOptions()
# Makes the test run in the terminal instead of the browser
options.add_argument("--headless")
# Gets the driver and defines its options
driver = webdriver.Chrome(executable_path=(os.getcwd() + "/../chromedriver" + exe), options=options)
# Navigates to the localhost, which is the site tested
driver.get("http://localhost:" + port + "/index.html")

print("")

# Runs all of the tests
InfoTest(driver)
SocialMediaTest(driver)
OpenDaysTest(driver)