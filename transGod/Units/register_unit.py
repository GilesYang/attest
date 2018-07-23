import unittest
from Browsers_Utils import Browser_Util, Url_Util, Alert_Message_Util, Message_Util
from Register_Control import register_control
import time



# global volumes

Exceptions = "No Exceptions"


class RegisterUnit(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.util = Browser_Util.Util()
        self.url = Url_Util.Url()
        self.alert_message = Alert_Message_Util.AlertMessage()
        self.contents = Message_Util.MessageContents()
        self.register = register_control.RegisterControl(self.util, self.url)

    def setUp(self):
        self.util.browser_start(self.url.PERSONAL_REGISTER_URL)

    def tearDown(self):
        self.util.browser_quit()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_login_link(self):
        """点击transgod个人版log跳转url"""
        try:
            self.register.login_link()
            self.util.timeImplay(10)
            self.current_window = self.util.current_window()
            self.util.switch_to_windows(self.current_window)
            self.new_url = self.util.current_url()
            print(self.new_url)
            self.assertEqual(self.new_url, self.url.HOMEPAGE_URL)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_usernameNull(self):
        """mobile == null"""
        self.alert_text_selector = '#webapp > div > div.uc-bg > div.uc-bg-top > div.uc-reg-box > div.reg-tel-box > div.reg-form > form > div:nth-child(1) > div.tooltip.top.toptel > div.tooltip-inner'
        try:
            self.register.usernameInput_null()
            self.util.timeImplay(10)
            self.alert_text = self.util.text_selector(self.alert_text_selector)
            self.assertEqual(self.alert_text, self.alert_message.mobile_null)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_userNotOnlyNumber(self):
        """Username Input Not Only Numbers"""
        try:
            self.register.usernameInput(self.contents.username_input_NotOnlyNumbers)
            self.util.timeImplay(10)
            self.alert_xpath = '//*[@id="webapp"]/div/div[3]/div[2]/div[2]/div[1]/div[3]/form/div[1]/div[2]/div[2]'
            self.alert_text = self.util.text_xpath(self.alert_xpath)
            print(self.alert_text)
            self.assertEqual(self.alert_text, self.alert_message.moible_type_error)
        except Exception as msg:
            raise
        else:
            print(Exceptions)

    def test_userNumber(self):
        """Username Input Not Numbers"""
        try:
            self.register.usernameInput(self.contents.username_input_NoNumber)
            self.util.timeImplay(10)
            self.alert_xpath = '//*[@id="webapp"]/div/div[3]/div[2]/div[2]/div[1]/div[3]/form/div[1]/div[2]/div[2]'
            self.alert_text = self.util.text_xpath(self.alert_xpath)
            print(self.alert_text)
            self.assertEqual(self.alert_text, self.alert_message.mobile_null)
        except Exception as msg:
            raise
        else:
            print(Exceptions)
