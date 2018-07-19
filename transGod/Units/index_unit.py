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
            pass
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)