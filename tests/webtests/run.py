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


# Opens a localhost server with the port 6969 and in the public directory
server = subprocess.Popen(["python" + pythonSubfix, "-m", "http.server",  "6969"],
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
# Gets the driver and defines its options
driver = webdriver.Chrome(executable_path=(os.getcwd() + "/../chromedriver" + exe), options=options)

driver.get("http://localhost:6969/index.html")

print("")

InfoTest(driver)
SocialMediaTest(driver)
OpenDaysTest(driver)