from selenium import webdriver
from colorama import Fore, Back, Style

class InfoTest:

    # The main function that gets the desired text and checks if it matches the reference text
    def checkInfoByID(self, id: str, refText: str, refHref: str, hasHref=True):
        # Gets the element text
        element = self.driver.find_element_by_id(id)
        elementHref = element.get_attribute("href")
        # Checks if the text includes the reference text
        assert refText in element.text
        if hasHref:
            assert elementHref == refHref
            print(element.text + ":", elementHref)
        else:
            print(element.text)
        print("-------------------------------------")

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        # Uses the imported colorama module to change the color of the output
        print('\033[1m' + Back.BLUE + "Startar test för kontaktinformation" + Style.RESET_ALL + '\033[0m')
        print("-------------------------------------")
        # Calls the function with the desired arguments
        self.checkInfoByID("title", "Stillhetens Spa", "", False)
        self.checkInfoByID("address", "Fjällgatan 32H", "https://goo.gl/maps/2aqFdNDscvCgKKQR9")
        self.checkInfoByID("zipCode", "981 39 KIRUNA", "https://goo.gl/maps/2aqFdNDscvCgKKQR9")
        self.checkInfoByID("phoneNumber", "0630‑555‑555", "tel:0630-555-555")
        self.checkInfoByID("mail", "info@thevikingtech.gitlab.io", "mailto:info@thevikingtech.gitlab.io")

        print("")
