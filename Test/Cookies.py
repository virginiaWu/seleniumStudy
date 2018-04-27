from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.example.com')

# Now set the cookie. This one's valid for entire domain
cookie = {'name': 'foo', 'value': 'bar'}
browser.add_cookie(cookie)

# And now output all the available cookies for the current URL
browser.get_cookies