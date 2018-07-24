import unittest
from Browsers_Utils import Browser_Util, Url_Util
from Login_Control import login_control

# global volumes
Exceptions = "No Exceptions"


class LoginUnit(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.util = Browser_Util.Util()
        self.url = Url_Util.Url()
        self.login = login_control.LoginControl(self.util, self.url)

    def setUp(self):
        self.util.browser_start(self.url.PERSONAL_LOGIN_URL)

    def tearDown(self):
        self.util.browser_quit()

    @classmethod
    def tearDownClass(cls):
        pass

