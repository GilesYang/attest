from selenium import webdriver
from enum import IntEnum
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Browsers(object):
    def util_start(self, url):
        # 使用Google Chrome作为webdriver驱动
        self.driver = webdriver.Chrome()
        # 访问url
        self.driver.get(url)
        # 屏幕自适应显示器最大化
        self.driver.maximize_window()

    def util_quit(self):
        self.static_sleep(Numbers.one_time)
        self.driver.quit()

    def function_sleep(self, number):
        time.sleep(number)

    # id
    def find_id(self, id):
        ids = (By.ID, id)
        WebDriverWait(self.driver, Numbers.twenty_time, Numbers.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_element_by_id(id)

    def click_id(self, id):
        self.find_id(id).click()

    def send_keys_id(self, id, message):
        self.find_id(id).send_keys(message)

    # xpath
    def find_xpath(self, xpath):
        xpaths = (By.XPATH, xpath)
        WebDriverWait(self.driver, Numbers.twenty_time, Numbers.half_time).until(ec.presence_of_element_located(xpaths))
        return self.driver.find_element_by_xpath(xpath)

    def click_xpath(self, xpath):
        self.find_xpath(xpath).click()

    def send_keys_xpath(self, xpath, message):
        self.find_xpath(xpath).send_keys(message)

    # name
    def find_name(self, name):
        names = (By.NAME, name)
        WebDriverWait(self.driver, Numbers.twenty_time, Numbers.half_time).until(ec.presence_of_element_located(names))
        return self.driver.find_element_by_name(name)

    def click_name(self, name):
        self.find_name(name).click()

    def send_keys_name(self, name, message):
        self.find_name(name).send_keys(message)

    # classname
    def find_classname(self, classname):
        classnames = (By.CLASS_NAME, classname)
        WebDriverWait(self.driver, Numbers.twenty_time, Numbers.half_time).until(ec.presence_of_element_located(classnames))
        return self.driver.find_element_by_class_name(classname)

    def click_classname(self, classname):
        self.find_classname(classname).click()

    def send_keys_classname(self, classname, message):
        self.find_classname(classname).send_keys(message)

class Numbers(IntEnum):
    half_time = 0.5
    one_time = 1
    twenty_time = 20