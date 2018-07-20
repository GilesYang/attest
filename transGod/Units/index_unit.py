import unittest
from Browsers_Utils import Browser_Util, Url_Util
from Index_Control import index_control
import time


Exceptions = "No Exceptions!"
class IndexUnit(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.util = Browser_Util.Util()
        self.url = Url_Util.Url()
        self.index = index_control.IndexControl(self.util)

    def setUp(self):
        self.util.browser_start(self.url.HOMEPAGE_URL)
        time.sleep(1)

    def tearDown(self):
        self.util.browser_quit()

    @classmethod
    def tearDownClass(cls):
        pass

    # 测试用例
    def test_topbar_personal(self):
        """topbar点击personal跳转url"""
        try:
            self.index.topbar_personal()
            time.sleep(2)
            self.current_url = self.util.current_url()
            print(self.current_url)
            self.personal_login_url = 'https://transgod.cn/ucenter/main/login'
            self.assertEqual(self.current_url, self.personal_login_url)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_topbar_team(self):
        """topbar点击team跳转url"""
        try:
            self.index.topbar_team()
            self.current_url = self.util.current_url()
            print(self.current_url)
            self.team_login_url = 'http://team.transgod.cn/cooperate/user/login'
            self.assertEqual(self.current_url, self.team_login_url)

        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)