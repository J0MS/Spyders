from selenium import webdriver

# To prevent download dialog
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', '/tmp')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

browser = webdriver.Firefox(profile)
#print type(browser)
url = raw_input('Enter a URL: ')
browser.get(url)
#browser.find_element_by_css_selector('p.content')

#browser.find_element_by_id('exportpt').click()
#browser.find_element_by_id('exporthlgt').click()
#URL = browser.find_element_by_tag_name('a')#.get_attribute('href')
#URL = ""
for a in browser.find_elements_by_xpath('/html/body'):
    print(a.get_attribute('href'))

for a in browser.find_elements_by_xpath('/html/body/div[8]/div[1]/div[1]/div/div/div[7]/p[2]/a[1]'):
    a.click()

#browser.switch_to.window('2147483649')
#print browser.window_handles

#print URL
#URL.click()
#browser.find_elements_by_xpath('/html/body/div[8]/div[1]/div[1]/div/div/div[7]/p[1]/a').get_attribute('href').find_element_by_link_text("80").click()
#driver.find_element_by_link_text("Available Deployments").click()
#browser.find_element_by_link_text("80").click()
