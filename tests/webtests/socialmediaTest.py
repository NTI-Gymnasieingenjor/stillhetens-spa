from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement
from colorama import Back, Style

class SocialMediaTest:
    # The main function that gets the class and href of the icons
    def checkIconsByClass(self, className: str, refHref: str):
        # Gets the class of the icons
        element: WebElement = self.driver.find_element_by_class_name(className)
        # Gets the href attribute of the icons
        elementHref = element.find_element_by_xpath('..').get_attribute("href")
        # Checks if the href links to the correct website
        assert elementHref == refHref
        # Replaces the "fa-" in the class name with a whitespace
        print(className.replace("fa-", "") + ":", elementHref)
    
        print("-------------------------------------")

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        # Uses the imported colorama module to change the color of the output
        print('\033[1m' + Back.BLUE + "Startar test för sociala medie-länkar" + Style.RESET_ALL + '\033[0m')
        print("-------------------------------------")

        self.checkIconsByClass("fa-facebook-square", "https://www.facebook.com/ntiuppsala")
        self.checkIconsByClass("fa-twitter-square", "https://twitter.com/ntiuppsala")
        self.checkIconsByClass("fa-instagram-square", "https://www.instagram.com/ntiuppsala")

        print("")
