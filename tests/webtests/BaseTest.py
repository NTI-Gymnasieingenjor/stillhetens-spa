import os
from selenium import webdriver 
import argparse
from sys import platform

if platform == "linux":
    exe=""
else:
    exe=".exe"
driver = webdriver.Chrome(executable_path=(os.getcwd() + "/../chromedriver" + exe))