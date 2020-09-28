from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement
from colorama import Back, Style


class InfoTest:
    # The main function that gets the desired text and checks if it matches the reference text
    def checkText(self, id: str, refText: str):
        # Gets the element text and sets it as a global variable to be able to access it from any function
        # The : WebElement sets a type hint which isn't required but makes the code more understandable 
        self.element: WebElement = self.driver.find_element_by_id(id)
        # Checks if the text includes the reference text
        assert refText in self.element.text
        print(self.element.text)

    def checkLink(self, id: str, refText: str, refLink: str):
        self.checkText(id, refText)
        elementHref = self.element.get_attribute("href")
        # Checks if the link is correct
        assert elementHref == refLink
        print(elementHref)
        print("-------------------------------------")

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        # Uses the imported colorama module to change the color of the output
        print('\033[1m' + Back.BLUE +
              "Startar test för kontaktinformation" + Style.RESET_ALL + '\033[0m')
        print("-------------------------------------")

        self.checkText("title", "Stillhetens spa")
        print("-------------------------------------")
        self.checkLink("address", "Fjällgatan 32H", "https://goo.gl/maps/2aqFdNDscvCgKKQR9")
        self.checkLink("zipCode", "981 39 KIRUNA", "https://goo.gl/maps/2aqFdNDscvCgKKQR9")
        self.checkLink("phoneNumber", "0630‑555‑555", "tel:0630-555-555")
        self.checkLink("mail", "info@thevikingtech.gitlab.io", "mailto:info@thevikingtech.gitlab.io")

        print("")
