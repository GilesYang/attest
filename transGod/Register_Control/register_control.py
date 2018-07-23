from Browsers_Utils import Browser_Util, Url_Util, Message_Util


class RegisterControl(object):
    def __init__(self, util, url):
        self.util = util
        self.url = url

    def login_link(self):
        self.logo_selector = '#webapp > div > div:nth-child(1) > div > header > div > div.navbar-header > a > span'
        self.util.click_selector(self.logo_selector)

    def usernameInput_null(self):
        self.login_button_selector = '#regtelBtn'
        self.util.click_selector(self.login_button_selector)

    def usernameInput(self, message):
        # volumes
        self.mobile_input_selector = '#reg-tel'
        self.username_input_selector = '#reg-tel-username'
        self.login_button_selector = '#regtelBtn'
        # active
        self.util.send_keys_selector(self.mobile_input_selector, message)
        self.util.click_selector(self.username_input_selector)
        self.util.click_selector(self.login_button_selector)

