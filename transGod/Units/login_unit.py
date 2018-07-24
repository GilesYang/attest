import unittest
from Browsers_Utils import Browser_Util, Url_Util, Message_Util, Alert_Message_Util
from Login_Control import login_control
# global volumes
Exceptions = "No Exceptions"


class LoginUnit(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.util = Browser_Util.Util()
        self.url = Url_Util.Url()
        self.login = login_control.LoginControl(self.util, self.url)
        self.contents = Message_Util.MessageContents()
        self.alert_message = Alert_Message_Util.AlertMessage()
    def setUp(self):
        self.util.browser_start(self.url.PERSONAL_LOGIN_URL)

    def tearDown(self):
        self.util.browser_quit()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_login_a(self):
        """username && password:null"""
        try:
            self.login.login_in("", "")
            self.util.timeImplay(10)
            self.alert_text = self.util.text_xpath('//*[@id="webapp"]/div/div[3]/div[2]/div[1]/div[3]/form/div[1]/div[2]/div[2]')
            print(self.alert_text)
            self.assertEqual(self.alert_text, self.contents.username_not_null_alert)
        except Exception as msg:
            raise
        else:
            print(Exceptions)

    def test_login_b(self):
        """username:null,password:123456"""
        try:
            self.login.login_in("", "123456")
            self.util.timeImplay(10)
            self.alert_text = self.util.text_xpath('//*[@id="webapp"]/div/div[3]/div[2]/div[1]/div[3]/form/div[1]/div[2]/div[2]')
            print(self.alert_text)
            self.assertEqual(self.alert_text, self.contents.username_not_null_alert)
        except Exception as msg:
            raise
        else:
            print(Exceptions)

    def test_login_c(self):
        """username:15011554977,password:null"""
        try:
            self.login.login_in(u"15011554977", "")
            self.util.timeImplay(10)
            self.alert_text = self.util.text_xpath('//*[@id="webapp"]/div/div[3]/div[2]/div[1]/div[3]/form/div[1]/div[2]/div[2]')
            print(self.alert_text)
            self.assertEqual(self.alert_text, self.contents.password_not_null_alert)
        except Exception as msg:
            raise
        else:
            print(Exceptions)

    def test_login_d(self):
        """username:15011554974,password:123456,button:relogin"""
        try:
            self.login.login_in(u"15011554974", u"123456")
            self.util.timeImplay(10)
            self.util.click_linktext("重新登录")
            self.current_url = self.util.current_url()
            print(self.current_url)
            self.assertEqual(self.current_url, self.url.PERSONAL_LOGIN_URL)
        except Exception as msg:
            raise
        else:
            print(Exceptions)

    def test_login_e(self):
        """username:15011554974,password:123456,button:toregister"""
        try:
            self.login.login_in(u"15011554974", u"123456")
            self.util.timeImplay(10)
            self.util.click_linktext("去注册")
            self.current_url = self.util.current_url()
            print(self.current_url)
            self.assertEqual(self.current_url, self.url.PERSONAL_LOGIN_URL)
        except Exception as msg:
            raise
        else:
            print(Exceptions)

    def test_login_g(self):
        """username:15011554977,password:123456888"""
        try:
            self.login.login_in(u"15011554977", u"123456888")
            self.util.timeImplay(10)
            self.current_url = self.util.current_url()
            print(self.current_url)
            self.assertEqual(self.current_url, self.url.PERSONAL_LOGIN_URL)
        except Exception as msg:
            raise
        else:
            print(Exceptions)

    def test_email_a(self):
        """email:null,password:null"""
        try:
            self.login.email_login("", "")
            self.util.timeImplay(10)
            self.alert_text = self.util.text_xpath('//*[@id="webapp"]/div/div[3]/div[2]/div[1]/div[3]/form/div[1]/div[2]/div[2]')
            print(self.alert_text)
            self.assertEqual(self.alert_text, self.contents.username_not_null_alert)
        except Exception as msg:
            raise
        else:
            print(Exceptions)

    def test_email_b(self):
        """email:null,password:123456"""
        try:
            self.login.email_login("", u"123456")
            self.util.timeImplay(10)
            self.alert_text = self.util.text_xpath('//*[@id="webapp"]/div/div[3]/div[2]/div[1]/div[3]/form/div[1]/div[2]/div[2]')
            print(self.alert_text)
            self.assertEqual(self.alert_text, self.contents.username_not_null_alert)
        except Exception as msg:
            raise
        else:
            print(Exceptions)

    def test_email_c(self):
        """email:15764512789@163.com,password:null"""
        try:
            self.login.email_login(u"15764512789@163.com", "")
            self.util.timeImplay(10)
            self.alert_text = self.util.text_xpath('//*[@id="webapp"]/div/div[3]/div[2]/div[1]/div[3]/form/div[1]/div[2]/div[2]')
            print(self.alert_text)
            self.assertEqual(self.alert_text, self.contents.password_not_null_alert)
        except Exception as msg:
            raise
        else:
            print(Exceptions)

    def test_email_d(self):
        """email:15764512789@163.com,password:123456 relogin"""
        try:
            self.login.email_login(u"15764512789@163.com", u"123456")
            self.util.timeImplay(10)
            self.util.click_linktext("重新登录")
            self.current_url = self.util.current_url()
            print(self.current_url)
            self.assertEqual(self.current_url, self.url.PERSONAL_LOGIN_URL)
        except Exception as msg:
            raise
        else:
            print(Exceptions)

    def test_email_e(self):
        """email:15764512789@163.com,password:123456 toregister"""
        try:
            self.login.email_login(u"15764512789@163.com", u"123456")
            self.util.timeImplay(10)
            self.util.click_linktext("去注册")
            self.current_url = self.util.current_url()
            print(self.current_url)
            self.assertEqual(self.current_url, self.url.PERSONAL_LOGIN_URL)
        except Exception as msg:
            raise
        else:
            print(Exceptions)

