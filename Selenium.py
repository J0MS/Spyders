import urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get('http://www.google.com')
#print "Ingrese"
#a = raw_input()
search = browser.find_element_by_name('q')
search.send_keys("tensorflow")
search.send_keys(Keys.RETURN)
#time.sleep(5) # sleep for 5 seconds so you can see the results

browser.quit()
