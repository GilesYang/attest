from Browsers_Utils import Browser_Util, Url_Util, Message_Util


class LoginControl(object):
    def __init__(self, util, url):
        self.util = util
        self.url = url



    def login_in(self, username, password):
        self.username_input_xpath = '//*[@id="login-tel"]'
        self.password_input_xpath = '//*[@id="login-password"]'
        self.login_button_xpath = '//*[@id="webapp"]/div/div[3]/div[2]/div[1]/div[3]/form/div[4]/button'
        self.util.send_keys_xpath(self.username_input_xpath, username)
        self.util.send_keys_xpath(self.password_input_xpath, password)
        self.util.click_xpath(self.login_button_xpath)

    def email_login(self, email, password):
        self.username_input_xpath = '//*[@id="login-tel"]'
        self.password_input_xpath = '//*[@id="login-password"]'
        self.login_button_xpath = '//*[@id="webapp"]/div/div[3]/div[2]/div[1]/div[3]/form/div[4]/button'
        self.util.send_keys_xpath(self.username_input_xpath, email)
        self.util.send_keys_xpath(self.password_input_xpath, password)
        self.util.click_xpath(self.login_button_xpath)