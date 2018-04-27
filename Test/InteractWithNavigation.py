from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://www.google.com")

element = browser.find_element_by_id("lst-ib")
element.send_keys("some text")
element.send_keys(" and some", Keys.ENTER)
browser.quit()