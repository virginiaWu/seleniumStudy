# The selenium package itself doesn't provide a testing tool/framework.
# You can write test case using Python's unittest module.

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class pythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.browser

        driver.get("http://www.python.org")
        elem = driver.find_element_by_id("id-search-field")
        elem.send_keys("pycon" + Keys.RETURN)



if __name__ == "__main__":
    unittest.main()
