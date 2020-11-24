from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

finp=input('enter item you want to search: ')
path='/Users/sashanksiwakoti/Desktop/python/selenium/chromedriver'
driver=webdriver.Chrome(path)
driver.get('https://hamrobazaar.com')
search=driver.find_element_by_name('searchword')
search.send_keys(finp)
search.send_keys(Keys.RETURN)
try:
    main=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//table')))
    #header1st=main.find_element_by_xpath('//table/tbody/tr[2]/td/table[4]/tbody/tr/td[2]/table[5]')
    for i in range(5, 21):
        header=main.find_element_by_xpath('//table/tbody/tr[2]/td/table[4]/tbody/tr/td[2]/table[%s]/tbody/tr[1]/td[3]/a[1]'%i)
        print(header.text)
finally:
    driver.quit()
#main=driver.find_element_by_xpath('//table')
#print(main.text)
#time.sleep(5)
