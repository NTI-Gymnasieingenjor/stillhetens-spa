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
        
    def checkImage(self, className:str, refSrc: str):
        # Gets the WebElement from the className and fetches the css property "background-image" and replaces the localhost url with an empty string
        elemSrc: WebElement = self.driver.find_element_by_class_name(className).value_of_css_property("background-image").replace("http://localhost:6969/assets/", "")
        assert elemSrc == refSrc
        print(refSrc)

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        # Uses the imported colorama module to change the color of the output
        print('\033[1m' + Back.BLUE + "Startar test för kontaktinformation" + Style.RESET_ALL + '\033[0m')
        print("-------------------------------------")

        print('\033[1m' + Back.GREEN + "Titlebar" + Style.RESET_ALL + '\033[0m')
        self.checkText("title", "Stillhetens spa")
        self.checkLink("phoneNumberTitlebar", "0630‑555‑555", "tel:0630-555-555")
        self.checkLink("navAnchor", "Öppettider", "http://localhost:6969/index.html#footer")
        print("-------------------------------------")

        print('\033[1m' + Back.GREEN + "Header" + Style.RESET_ALL + '\033[0m')
        self.checkImage("head", 'url("alex-bertha-Jyg7xHRmXiU-unsplash.jpg")')
        self.checkText("headerSlogan", "En unik och avkopplande upplevelse");
        print("-------------------------------------")

        print('\033[1m' + Back.GREEN + "Footer" + Style.RESET_ALL + '\033[0m')
        self.checkLink("address", "Fjällgatan 32H\n981 39 KIRUNA", "https://goo.gl/maps/2aqFdNDscvCgKKQR9")
        self.checkLink("phoneNumber", "0630‑555‑555", "tel:0630-555-555")
        self.checkLink("mail", "info@thevikingtech.gitlab.io", "mailto:info@thevikingtech.gitlab.io")
        print("-------------------------------------")

        print("")
