from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
path='/Users/sashanksiwakoti/Desktop/python/selenium/chromedriver'
driver=webdriver.Chrome(path)
driver.get('https://hamrobazaar.com')
search=driver.find_element_by_name('searchword')
search.send_keys('duke 250')
search.send_keys(Keys.RETURN)
main=driver.find_element_by_xpath('//table')
print(main.text)
#time.sleep(5)
driver.quit()
