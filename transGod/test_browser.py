from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://transgod.cn/ucenter/main/reg")
time.sleep(1)
driver.find_element_by_id('reg-tel').send_keys('atman123')
time.sleep(1)

if driver.find_element_by_id('reg-tel').get_attribute('placeholder') != "手机号":
    print("Success")
    driver.close()
    driver.quit()
else:
    print("Failed")
    driver.quit()