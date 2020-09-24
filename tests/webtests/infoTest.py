from selenium import webdriver 

class InfoTest:
    def __init__(self, driver: webdriver.Chrome):
        
        title = driver.find_element_by_id("title").text

        assert "Stillhetens Spa" in title 
        print(title)
