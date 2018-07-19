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
        self.driver.quit()