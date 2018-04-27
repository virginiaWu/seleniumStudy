from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # The key class provide keys in the keyboard like RETURN, F1, ALT etc.

browser = webdriver.Chrome()

browser.get('http://www.python.org')
assert 'Python' in browser.title

elem = browser.find_element_by_name('q')  # Find the search box
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No result found." not in browser.page_source
browser.quit()