from Browsers_Utils import Browser_Util, Url_Util

class IndexControl(object):
    def __init__(self, util, url):
        self.util = util
        self.url = url

    def topbar_personal(self):
        self.personal_selector = 'body > div.index-box > header > section > nav > ul > li:nth-child(1) > a'
        self.util.click_selector(self.personal_selector)
        # self.topbar_xpath = self.util.find_group_xpath('/html/body/div[1]/header/section/nav/ul')
        # print(self.topbar_xpath)
        # for i in range(1, len(self.topbar_xpath), 1):
        #     self.util.click_xpath(self.topbar_xpath[i])
        #     self.util.url_back()

    def topbar_team(self):
        self.team_selector = 'body > div.index-box > header > section > nav > ul > li:nth-child(2) > a'
        self.util.click_selector(self.team_selector)

    def topbar_apimarket(self):
        self.api_selector = 'body > div.index-box > header > section > nav > ul > li:nth-child(3) > a'
        self.util.click_selector(self.api_selector)

    def topbar_trados(self):
        self.trados_selector = 'body > div.index-box > header > section > nav > ul > li:nth-child(4) > a'
        self.util.click_selector(self.trados_selector)

    def topbar_about(self):
        self.about_selector = 'body > div.index-box > header > section > nav > ul > li:nth-child(5) > a'
        self.util.click_selector(self.about_selector)

    def topbar_help(self):
        self.help_selector = 'body > div.index-box > header > section > nav > ul > li:nth-child(6) > a'
        self.util.click_selector(self.help_selector)

    def topbar_login(self):
        self.login_selector = 'body > div.index-box > header > section > div.sign-in-group.pull-right.clearfix > a.trans-btn.size-m.pull-left'
        self.util.click_selector(self.login_selector)

    def topbar_register(self):
        self.register_selector = 'body > div.index-box > header > section > div.sign-in-group.pull-right.clearfix > a.trans-btn.size-m.trans-btn-classic.pull-right'
        self.util.click_selector(self.register_selector)

    def trans(self):
        self.trans_selector = 'body > div.index-box > div > section.section-box.support.bg-gray > div > div:nth-child(1) > p > a > strong'
        self.util.click_selector(self.trans_selector)

    def trans_file(self):
        self.trans_file_selector = 'body > div.index-box > div > section.section-box.support.bg-gray > div > div:nth-child(2) > p > a > strong'
        self.util.click_selector(self.trans_file_selector)

    def personal_cat(self):
        self.personal_cat_selector = 'body > div.index-box > div > section.section-box.support.bg-gray > div > div:nth-child(3) > p > a > strong'
        self.util.click_selector(self.personal_cat_selector)

    def team_cat(self):
        self.team_cat_selector = 'body > div.index-box > div > section.section-box.support.bg-gray > div > div:nth-child(4) > p > a > strong'
        self.util.click_selector(self.team_cat_selector)

    def engine_personal(self):
        self.engine_personal_selector = 'body > div.index-box > div > section.section-box.support.bg-gray > div > div.support-item.col-xs-2.hot > p > a > strong'
        self.util.click_selector(self.engine_personal_selector)

    def topbar_personal_login(self):
        self.login_personal_xpath = '/html/body/div[1]/header/section/nav/ul/li[1]/a'
        self.login_button_selector = 'body > div.index-box > header > section > div.sign-in-group.pull-right.clearfix > a.trans-btn.size-m.pull-left'
        self.util.click_selector(self.login_button_selector)
        self.util.login_personal(u'15011554977', u'123456')
        if self.util.current_url() == self.url.HOMEPAGE_URL:
            print(self.url.HOMEPAGE_URL)
            self.util.click_xpath(self.login_personal_xpath)
        else:
            print("The Url is Error!")

    def topbar_team_login(self):
        self.login_team_selector = 'body > div.index-box > header > section > nav > ul > li:nth-child(2) > a'
        self.util.click_selector(self.login_team_selector)
        self.util.login_team(u'15011554977', u'123456')
        if self.util.current_url() == self.url.HOMEPAGE_URL:
            print(self.url.HOMEPAGE_URL)
            self.util.click_selector(self.login_team_selector)
        else:
            print("The Url is Error!")

    def trans_login(self):
        self.trans_selector = 'body > div.index-box > div > section.section-box.support.bg-gray > div > div:nth-child(1) > p > a > strong'
        self.login_button_selector = 'body > div.index-box > header > section > div.sign-in-group.pull-right.clearfix > a.trans-btn.size-m.pull-left'
        self.util.click_selector(self.login_button_selector)
        self.util.login_personal(u'15011554977', u'123456')
        if self.util.current_url() == self.url.HOMEPAGE_URL:
            print(self.url.HOMEPAGE_URL)
            self.util.click_selector(self.trans_selector)
        else:
            print("The Url is Error!")

    def trans_file_login(self):
        self.trans_file_selector = 'body > div.index-box > div > section.section-box.support.bg-gray > div > div:nth-child(2) > p > a > strong'
        self.login_button_selector = 'body > div.index-box > header > section > div.sign-in-group.pull-right.clearfix > a.trans-btn.size-m.pull-left'
        self.util.click_selector(self.login_button_selector)
        self.util.login_personal(u'15011554977', u'123456')
        if self.util.current_url() == self.url.HOMEPAGE_URL:
            print(self.url.HOMEPAGE_URL)
            self.util.click_selector(self.trans_file_selector)
        else:
            print("The Url is Error!")

    def personal_cat_login(self):
        self.personal_cat_xpath = '/html/body/div[1]/div/section[2]/div/div[3]/p/a'
        self.login_button_selector = 'body > div.index-box > header > section > div.sign-in-group.pull-right.clearfix > a.trans-btn.size-m.pull-left'
        self.util.click_selector(self.login_button_selector)
        self.util.login_personal(u'111', u'111')
        if self.util.current_url() == self.url.HOMEPAGE_URL:
            print("The Url is True!")
            self.util.click_xpath(self.personal_cat_xpath)
        else:
            print("The Url is Error!")

    def team_cat_login(self):
        self.team_cat_xpath = '/html/body/div[1]/div/section[2]/div/div[4]/p/a'
        self.team_logo_selector = '#webapp > div > div:nth-child(1) > div:nth-child(2) > header > div > div > a > span'
        self.util.click_xpath(self.team_cat_xpath)
        self.util.login_team(u'15011554977', u'111')
        self.util.click_selector(self.team_logo_selector)
        self.current_window = self.util.current_window()
        self.switch_window = self.util.switch_to_windows(self.current_window)
        self.util.click_selector(self.team_cat_xpath)

    def index_link_johnson(self):
        self.johnson_selector = 'body > div.index-box > div > section.section-box.client > div:nth-child(2) > a:nth-child(1) > i'
        self.util.click_selector(self.johnson_selector)

    def index_link_news(self):
        self.news_selector = 'body > div.index-box > div > section.section-box.client > div:nth-child(2) > a:nth-child(2) > i'
        self.util.click_selector(self.news_selector)

    def index_link_peking(self):
        self.peking_selector = 'body > div.index-box > div > section.section-box.client > div:nth-child(2) > a:nth-child(3) > i'
        self.util.click_selector(self.peking_selector)

    def index_link_tsinghua(self):
        self.tsinghua_selector = 'body > div.index-box > div > section.section-box.client > div:nth-child(2) > a:nth-child(4) > i'
        self.util.click_selector(self.tsinghua_selector)

    def index_link_shenrong(self):
        self.shenrong_selector = 'body > div.index-box > div > section.section-box.client > div.client-list.multiple-line > a:nth-child(1) > i'
        self.util.click_selector(self.shenrong_selector)

    def index_link_wanfang(self):
        self.wanfang_selector = 'body > div.index-box > div > section.section-box.client > div.client-list.multiple-line > a:nth-child(2) > i'
        self.util.click_selector(self.wanfang_selector)

    def index_link_taimei(self):
        self.taimei_selector = 'body > div.index-box > div > section.section-box.client > div.client-list.multiple-line > a:nth-child(3) > i'
        self.util.click_selector(self.taimei_selector)

    def footer_atman(self):
        self.footer_atman_xpath = "/html/body/div[1]/footer/section[1]/div/div[1]/ul/li[5]/a"
        self.util.click_xpath(self.footer_atman_xpath)

    def footer_center(self):
        self.footer_center_xpath = "/html/body/div[1]/footer/section[1]/div/div[1]/ul/li[4]/a"
        self.util.click_xpath(self.footer_center_xpath)

    def footer_media(self):
        self.footer_media_xpath = "/html/body/div[1]/footer/section[1]/div/div[1]/ul/li[3]/a"
        self.util.click_xpath(self.footer_media_xpath)

    def footer_join(self):
        self.footer_join_xpath = "/html/body/div[1]/footer/section[1]/div/div[1]/ul/li[2]/a"
        self.util.click_xpath(self.footer_join_xpath)

    def footer_message(self):
        self.footer_message_xpath = "/html/body/div[1]/footer/section[1]/div/div[1]/ul/li[1]/a"
        self.util.click_xpath(self.footer_message_xpath)

    def footer_TMXMall(self):
        self.footer_TMX_xpath = "/html/body/div[1]/footer/section[1]/div/div[1]/p[2]/a[1]"
        self.util.click_xpath(self.footer_TMX_xpath)

    def footer_Ucloud(self):
        self.footer_ucloud_xpath = "/html/body/div[1]/footer/section[1]/div/div[1]/p[2]/a[2]"
        self.util.click_xpath(self.footer_ucloud_xpath)