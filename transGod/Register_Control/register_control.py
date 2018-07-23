from Browsers_Utils import Browser_Util, Url_Util


class RegisterControl(object):
    def __init__(self, url, util):
        self.util = util
        self.url = url

    def login_link(self):
        self.logo_selector = '#webapp > div > div:nth-child(1) > div > header > div > div.navbar-header > a > span'
        self.util.click_selector(self.logo_selector)

    def mobile_null(self):
        self.login_button_selector = '#regtelBtn'
        self.util.click_selector(self.login_button_selector)