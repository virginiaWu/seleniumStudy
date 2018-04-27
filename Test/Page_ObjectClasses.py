from selenium import BasePageElement
from locations import MainPageLocators

class searchTextElement(BasePageElement):
    locator = 'q'

class BasePage(object):
    def __init__(self):
        self.driver = driver