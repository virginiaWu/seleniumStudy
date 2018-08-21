from selenium import BasePageElement

class searchTextElement(BasePageElement):
    locator = 'q'

class BasePage(object):
    def __init__(self):
        self.driver = driver