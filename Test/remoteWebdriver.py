from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

browser = webdriver.Remote(
    command_executor = 'http://127.0.0.1:4444/wd/hub',
    desired_capabilities = DesiredCapabilities.CHROME
)

browser = webdriver.Remote(
    command_executor = 'http://127.0.0.1:4444/wd/hub',
    desired_capabilities = DesiredCapabilities.OPERA
)
browser = webdriver.Remote(
    command_executor = 'http://127.0.0.1:4444/wd/hub',
    desired_capabilities = DesiredCapabilities.HTMLUNITWITHJS
)