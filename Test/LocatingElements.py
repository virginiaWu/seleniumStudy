from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000/Test.html')

# Locating by id
login_form = browser.find_element_by_id("loginForm")

# Locating by Name
username = browser.find_element_by_name('username')
username = browser.find_element_by_name('password')
continue_button = browser.find_element_by_name('continue')

# Locating by XPath
username = browser.find_element_by_xpath("//form[input/@name='username']")
username = browser.find_element_by_xpath("//form[@id='loginForm']/input[1]")
username = browser.find_element_by_xpath("//input[@name='username']")

clear_button = browser.find_element_by_xpath("//input[@name='continue'][@type='button']")
clear_button = browser.find_element_by_xpath("//form[@id='loginForm']/input[4]")

# Locating Hyperlinks by Link Text
continue_link = browser.find_element_by_link_text('Go To Baidu')
continue_link = browser.find_element_by_partial_link_text('Bai')

# Locating by Tag Name
heading1 = browser.find_element_by_tag_name('h1')

# Locating by Class Name
content = browser.find_element_by_class_name('content')

# Locating by css selector
content = browser.find_element_by_css_selector('h1.content')

browser.quit()

