from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path='/Users/sashanksiwakoti/Desktop/python/selenium/chromedriver'
driver=webdriver.Chrome(path)
driver.get('https://hamrobazaar.com')
search=driver.find_element_by_name('searchword')
search.send_keys('duke 250')
search.send_keys(Keys.RETURN)
try:
    main=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//table')))
    print(main.text)

finally:
    driver.quit()
#main=driver.find_element_by_xpath('//table')
#print(main.text)
#time.sleep(5)
