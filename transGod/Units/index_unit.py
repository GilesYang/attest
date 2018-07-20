import unittest
from Browsers_Utils import Browser_Util, Url_Util
from Index_Control import index_control
import time


# global volumes

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
            self.util.timeImplay(10)
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
            self.util.timeImplay(10)
            self.current_url = self.util.current_url()
            print(self.current_url)
            self.team_login_url = 'http://team.transgod.cn/cooperate/user/login'
            self.assertEqual(self.current_url, self.team_login_url)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_topbar_apimarket(self):
        """topbar点击api跳转url"""
        try:
            self.index.topbar_apimarket()
            self.util.timeImplay(10)
            self.current_window = self.util.current_window()
            self.util.switch_to_windows(self.current_window)
            self.new_url = self.util.current_url()
            print(self.new_url)
            self.api_url = 'https://market.aliyun.com/products/57124001/cmapi028086.html#sku=yuncode2208600000'
            self.assertEqual(self.new_url, self.api_url)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_topbar_trados(self):
        """topbar点击trados跳转url"""
        try:
            self.index.topbar_trados()
            self.util.timeImplay(10)
            self.current_window = self.util.current_window()
            self.util.switch_to_windows(self.current_window)
            self.new_url = self.util.current_url()
            print(self.new_url)
            self.trados_url = 'http://team.transgod.cn/trados'
            self.assertEqual(self.new_url, self.trados_url)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_topbar_aboutus(self):
        """topbar点击about us跳转url"""
        try:
            self.index.topbar_about()
            self.util.timeImplay(10)
            self.current_window = self.util.current_window()
            self.util.switch_to_windows(self.current_window)
            self.new_url = self.util.current_url()
            print(self.new_url)
            self.atman_url = 'http://atman.ai/'
            self.assertEqual(self.new_url, self.atman_url)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_topbar_help(self):
        """topbar点击help跳转url"""
        try:
            self.index.topbar_help()
            self.util.timeImplay(10)
            self.current_window = self.util.current_window()
            self.util.switch_to_windows(self.current_window)
            self.new_url = self.util.current_url()
            print(self.new_url)
            self.help_url = 'https://intercom.help/transgod'
            self.assertEqual(self.new_url, self.help_url)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_topbar_login(self):
        """topbar点击login跳转url"""
        try:
            self.index.topbar_login()
            self.util.timeImplay(10)
            self.current_url = self.util.current_url()
            print(self.current_url)
            self.assertEqual(self.current_url, 'https://transgod.cn/ucenter/main/login')
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_topbar_register(self):
        """topbar点击register跳转url"""
        try:
            self.index.topbar_register()
            self.util.timeImplay(10)
            self.current_url = self.util.current_url()
            print(self.current_url)
            self.assertEqual(self.current_url, 'https://transgod.cn/ucenter/main/reg')
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_trans(self):
        """未登录状态,点击翻译文字跳转url"""
        try:
            self.index.trans()
            self.util.timeImplay(10)
            self.current_window = self.util.current_window()
            self.util.switch_to_windows(self.current_window)
            self.new_url = self.util.current_url()
            print(self.new_url)
            self.current_url = 'https://transgod.cn/opt/trans'
            self.assertEqual(self.new_url, self.current_url)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_trans_file(self):
        """未登录状态,点击翻译文件跳转url"""
        try:
            self.index.trans_file()
            self.util.timeImplay(10)
            self.current_window = self.util.current_window()
            self.util.switch_to_windows(self.current_window)
            self.new_url = self.util.current_url()
            print(self.new_url)
            self.current_url = 'https://transgod.cn/opt/trans?type=file'
            self.assertEqual(self.new_url, self.current_url)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_personal_cat(self):
        """未登录状态,点击个人版cat跳转url"""
        try:
            self.index.personal_cat()
            self.util.timeImplay(10)
            self.new_url = self.util.current_url()
            print(self.new_url)
            self.current_url = 'https://transgod.cn/ucenter/main/login'
            self.assertEqual(self.new_url, self.current_url)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_team_cat(self):
        """未登录状态,点击团队版cat跳转url"""
        try:
            self.index.team_cat()
            self.util.timeImplay(10)
            self.new_url = self.util.current_url()
            print(self.new_url)
            self.current_url = 'http://team.transgod.cn/cooperate/user/login'
            self.assertEqual(self.new_url, self.current_url)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_engine_personal(self):
        """未登录状态点击engine跳转url"""
        try:
            self.index.engine_personal()
            self.util.timeImplay(10)
            self.current_window = self.util.current_window()
            self.util.switch_to_windows(self.current_window)
            self.new_url = self.util.current_url()
            print(self.new_url)
            self.current_url = 'http://team.transgod.cn/cooperate/user/login'
            self.assertEqual(self.new_url, self.current_url)

        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_topbar_personal_login(self):
        """登陆状态点击topbar个人跳转url"""
        try:
            self.index.topbar_personal_login()
            self.util.timeImplay(10)
            self.new_url = self.util.current_url()
            print(self.new_url)
            self.current_url = 'https://transgod.cn/project'
            self.assertEqual(self.new_url, self.current_url)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_topbar_team_login(self):
        """登陆状态点击topbar团队跳转url"""
        try:
            self.index.topbar_team_login()
            self.util.timeImplay(10)
            self.new_url = self.util.current_url()
            print(self.new_url)
            self.current_url = 'https://transgod.cn/cooperate/user/login'
            self.assertEqual(self.new_url, self.current_url)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)

    def test_trans_login(self):
        """登陆状态点击翻译文字跳转url"""
        try:
            self.index.trans_login()
            self.util.timeImplay(10)
            self.current_window = self.util.current_window()
            self.util.switch_to_windows(self.current_window)
            self.topbar_logo_selector = '#webapp > div > div:nth-child(1) > div > header > div > div > a > span'
            self.logo_text = self.util.text_selector(self.topbar_logo_selector)
            print(self.logo_text)
            self.current_text = "TransGod"
            self.assertEqual(self.logo_text, self.current_text)
        except Exception as msg:
            print(msg)
        else:
            print(Exceptions)