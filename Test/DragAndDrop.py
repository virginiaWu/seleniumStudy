from selenium import webdriver
from selenium.webdriver import ActionChains
# 模拟鼠标操作，比如：单击 双击 点击鼠标右键 拖拽等，selenium提供了一个类来处理这类事件-ActionChains
browser = webdriver.Chrome()
browser.get("http://localhost:8000/Test.html")

element = browser.find_element_by_name("source")
target = browser.find_element_by_name("target")

action_chains = ActionChains(browser)
action_chains.drag_and_drop(element, target).perform()


browser.switch_to_window(browser.window_handles[1])
