from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://transgod.cn")
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/span').click()
time.sleep(2)
driver.quit()