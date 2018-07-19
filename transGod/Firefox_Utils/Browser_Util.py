from selenium import webdriver
from enum import IntEnum
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Util(object):
    def firefox_start(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()

    def firefox_close(self):
        self.sleep(Enum.two_time)
        self.driver.quit()

    def sleep(self, number):
        time.sleep(number)

    def timeImplay(self,number):
        self.driver.implicitly_wait(number)

    def mouse_move(self, xpath):
        ActionChains(self.driver).move_to_element(self.find_xpath(xpath)).perform()

    # 按照索引查找
    def selectIndex(self, xpath, number):
        Select(self.find_xpath(xpath)).select_by_index(number)
        self.click_xpath(xpath)

    def key_enter(self, xpath):
        self.find_xpath(xpath).send_keys(Keys.ENTER)

    def find_id(self, id):
        ids = (By.ID, id)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_element_by_id(id)

    def click_id(self, id):
        self.find_id(id).click()

    def send_keys_id(self, id, message):
        self.find_id(id).send_keys(message)

    def text_id(self, id):
        return self.find_id(id).text

    def title_id(self):
        return self.driver.title

    def find_xpath(self, xpath):
        ids = (By.XPATH, xpath)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_element_by_xpath(xpath)

    def click_xpath(self, xpath):
        self.find_xpath(xpath).click()

    def send_keys_xpath(self, xpath, message):
        self.find_xpath(xpath).send_keys(message)

    def text_xpath(self, xpath):
        return self.find_xpath(xpath).text

    def find_classname(self, classname):
        ids = (By.CLASS_NAME, classname)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_element_by_class_name(classname)

    def click_classname(self, classname):
        self.find_classname(classname).click()

    def send_keys_classname(self, classname, message):
        self.find_classname(classname).send_keys(message)

    def text_classname(self, classname):
        return self.find_classname(classname).text

    def find_selector(self, selector):
        ids = (By.CSS_SELECTOR, selector)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_element_by_css_selector(selector)

    def click_selector(self, selector):
        self.find_selector(selector).click()

    def send_keys_selector(self, selector, message):
        self.find_selector(selector).send_keys(message)

    def text_selector(self, selector):
        return self.find_selector(selector).text

    def find_tag(self, tag):
        ids = (By.TAG_NAME, tag)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_element_by_tag_name(tag)

    def click_tag(self, tag):
        self.find_tag(tag).click()

    def send_keys_tag(self, tag, message):
        self.find_tag(tag).send_keys(message)

    def text_tag(self, tag):
        return self.find_tag(tag).text

    def find_linktext(self, link):
        ids = (By.LINK_TEXT, link)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_element_by_link_text(link)

    def click_linktext(self, link):
        self.find_linktext(link).click()

    def send_keys_linktext(self, link, message):
        self.find_linktext(link).send_keys(message)

    def text_linktext(self, link):
        return self.find_linktext(link).text

    def find_partial(self, partial):
        ids = (By.PARTIAL_LINK_TEXT, partial)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_element_by_partial_link_text(partial)

    def click_partial(self, partial):
        self.find_partial(partial).click()

    def send_keys_partial(self, partial, message):
        self.find_partial(partial).send_keys(message)

    def text_partial(self, partial):
        return self.find_partial(partial).text

    def get_attribute_id(self, id, attributes):
        self.driver.find_element_by_id(id).get_attribute(attributes)

    def get_attribute_xpath(self, xpath, attributes):
        self.driver.find_element_by_xpath(xpath).get_attribute(attributes)

    def switch_to_frame_id(self, id):
        self.driver.switch_to_frame(self.find_id(id))

    def switch_to_frame_classname(self, classname):
        self.driver.switch_to_frame(self.find_classname(classname))

    def switch_to_frame_xpath(self, xpath):
        self.driver.switch_to_frame(self.find_xpath(xpath))

    def switch_to_frame_tagname(self, tag):
        self.driver.switch_to_frame(self.find_tag(tag))

    def switch_to_frame_linktext(self, link):
        self.driver.switch_to_frame(self.find_linktext(link))

    def switch_to_frame_selector(self, selector):
        self.driver.switch_to_frame(self.find_selector(selector))

    def switch_to_content(self):
        self.driver.switch_to_default_content()

    def current_window(self):
        return self.driver.current_window_handle

    def switch_to_windows(self, current_window):
        all_window = self.driver.window_handles
        for window in all_window:
            if window != current_window:
                self.driver.switch_to_window(window)
        print("switch to window successfully!")

    def find_group_id(self, id):
        ids = (By.ID, id)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_elements_by_id(id)

    def click_group_id(self, id, index):
        self.find_group_id(id)[index].click()

    def send_keys_group_id(self, id, index, message):
        self.find_group_id(id)[index].send_keys(message)

    def text_group_id(self, id, index):
        return self.find_group_id(id)[index].text

    def find_group_xpath(self, xpath):
        ids = (By.XPATH, xpath)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_elements_by_xpath(xpath)

    def click_group_xpath(self, index, xpath):
        self.find_group_xpath(xpath)[index].click()

    def send_keys_group_xpath(self, index, xpath, message):
        self.find_group_xpath(xpath)[index].send_keys(message)

    def text_group_xpath(self, index, xpath):
        return self.find_group_xpath(xpath)[index].text

    def find_group_classname(self, classname):
        ids = (By.CLASS_NAME, classname)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_elements_by_class_name(classname)

    def click_group_classname(self, classname, index):
        self.find_group_classname(classname)[index].click()

    def send_keys_group_classname(self, classname, index, message):
        self.find_group_classname(classname)[index].send_keys(message)

    def text_group_classname(self, index, classname):
        return self.find_group_classname(classname)[index].text

    def find_group_selector(self, selector):
        ids = (By.CSS_SELECTOR, selector)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_elements_by_css_selector(selector)

    def click_group_selector(self, selector, index):
        self.find_group_selector(selector)[index].click()

    def send_keys_group_selector(self, selector, index, message):
        self.find_group_selector(selector)[index].send_keys(message)

    def text_group_selector(self, selector, index):
        return self.find_group_selector(selector)[index].text

    def find_group_linktext(self, link):
        ids = (By.LINK_TEXT, link)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_elements_by_link_text(link)

    def click_group_linktext(self, link, index):
        self.find_group_linktext(link)[index].click()

    def send_keys_group_linktext(self, link, index, message):
        self.find_group_linktext(link)[index].send_keys(message)

    def text_group_linktext(self, link, index):
        return self.find_group_linktext(link)[index].text

    def find_group_partial(self, partial):
        ids = (By.PARTIAL_LINK_TEXT, partial)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_elements_by_partial_link_text(partial)

    def click_group_partial(self, partial, index):
        self.find_group_partial(partial)[index].click()

    def send_keys_group_partial(self, partial, index, message):
        self.find_group_partial(partial)[index].send_keys(message)

    def text_group_partial(self, partial, index):
        return self.find_group_partial(partial)[index].text

    def find_group_tag(self, tag):
        ids = (By.TAG_NAME, tag)
        WebDriverWait(self.driver, Enum.twenty_time, Enum.half_time).until(ec.presence_of_element_located(ids))
        return self.driver.find_elements_by_tag_name(tag)

    def click_group_tag(self, tag, index):
        self.find_group_tag(tag)[index].click()

    def send_keys_group_tag(self, tag, index, message):
        self.find_group_tag(tag)[index].send_keys(message)

    def text_group_tag(self, tag, index):
        return self.find_group_tag(tag)[index].text

    def current_url(self):
        self.url = self.driver.current_url
        return self.url

    def ass(self):
        self.picture = self.driver.get_screenshot_as_png()
        print("%s", self.picture)

    def gettitle(self):
        return self.driver.title

    def switch_alert(self):
        self.driver.switch_to_alert()

    # 登陆操作
    def login_in(self):
        self.send_keys_id('login-tel', u"15011554977")
        self.send_keys_id('login-password', u"123456")
        self.click_xpath('//*[@id="webapp"]/div/div[3]/div[2]/div[1]/div[3]/form/div[4]/button')


class Enum(IntEnum):
    point_one_time = 0.1
    half_time = 0.5
    one_time = 1
    two_time = 2
    three_time = 3
    five_time = 5
    ten_time = 10
    twenty_time = 20
    fifty_time = 50
    hundred_time = 100
