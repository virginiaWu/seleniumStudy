from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get("http://localhost:8000/Test.html")

element = browser.find_element_by_name('name')
all_options = element.find_elements_by_tag_name('option')
for option in all_options:
    print("Value is : %s" % option.get_attribute("value"))
    option.click()
    time.sleep(5)

select = Select(browser.find_elements_by_tag_name('name'))
select.deselect_all() #取消所选的option
