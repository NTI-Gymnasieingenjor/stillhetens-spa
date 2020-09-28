from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement
from colorama import Back, Style


class OpenDaysTest:

    # The main function that gets the desired text and checks if it matches the reference text
    def checkInfoByID(self, id: str, refDay: str, dateText: str):
        # Gets the children of the element
        elements: list[WebElement] = self.driver.find_element_by_id(id).find_elements_by_xpath(".//*")
        # Checks if the gotten values match the reference strings
        assert refDay == elements[0].text and dateText == elements[1]
        print("-------------------------------------")

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        # Uses the imported colorama module to change the color of the output
        print('\033[1m' + Back.BLUE + "Startar test för Öppentider" + Style.RESET_ALL + '\033[0m')
        print("-------------------------------------")

        self.checkInfoByID("weekdays", "Mån-Fre", "10‑16")
        self.checkInfoByID("saturday", "Lördag", "12‑15")
        self.checkInfoByID("sunday", "Söndag", "Stängt")

        print("")
