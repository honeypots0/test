from selenium import webdriver

browser = webdriver.Firefox()
 
 
# remember to include .xpi at the end of your file names 
browser.install_addon("hello.xpi", temporary=True)
 
browser.get('http://www.yahoo.com')
 