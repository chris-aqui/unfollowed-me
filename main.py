from selenium import webdriver
# from time import sleep
# from secrets import pw

class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")

InstaBot()