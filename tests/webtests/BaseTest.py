import os
from selenium import webdriver 
import argparse

print()
driver = webdriver.Chrome(os.getcwd() + "/../chromedriver")