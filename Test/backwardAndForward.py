from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://www.google.com')
browser.get('http://www.baidu.com')
browser.back()
time.sleep(3)
browser.forward()