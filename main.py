from webbot import Browser
# This will open the chromium-browser
# (Also, "web" can be anything as long as you change each reference of it as well)
web = Browser()
# This will open the following website in the tab that was opened
web.go_to('https://www.google.com/')
web.type('welcome to no goguardian browser')
