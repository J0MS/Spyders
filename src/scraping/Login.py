from selenium import webdriver

# To prevent download dialog
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', '/tmp')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

browser = webdriver.Firefox(profile)

browser.get("https://github.com/login")

username = browser.find_element_by_id('login_field')
password = browser.find_element_by_id('password')
username.send_keys("passwd@ciencias.unam.mx")
password.send_keys("reddata54")
#buttonLogin = browser.find_elements_by_xpath('/html/body/div[3]/div[1]/div/form/div[4]/input[3]')
#buttonLogin.click()

for a in browser.find_elements_by_xpath('/html/body/div[3]/div[1]/div/form/div[4]/input[3]'):
    a.click()
