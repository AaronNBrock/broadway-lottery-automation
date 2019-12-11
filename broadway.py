import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://lottery.broadwaydirect.com/')
print('To be continued...')
time.sleep(5)
driver.quit()
