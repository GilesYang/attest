from Browsers_Utils import Browser_Util, Url_Util

class IndexControl(object):
    def __init__(self, util):
        self.util = util

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
        self.login_personal_selector = 'body > div.index-box > header > section > nav > ul > li:nth-child(1) > a'
        self.login_button_selector = 'body > div.index-box > header > section > div.sign-in-group.pull-right.clearfix > a.trans-btn.size-m.pull-left'
        self.util.click_selector(self.login_button_selector)
        self.util.login_personal(u'15011554977', u'123456')
        if self.util.current_url() == 'https://transgod.cn':
            print("The Url is True!")
            self.util.click_selector(self.login_personal_selector)
        else:
            print("The Url is Error!")

    def topbar_team_login(self):
        self.login_team_selector = 'body > div.index-box > header > section > nav > ul > li:nth-child(2) > a'
        self.util.click_selector(self.login_team_selector)
        self.util.login_team(u'15011554977', u'123456')
        if self.util.current_url() == 'https://transgod.cn':
            print("The Url is Ture!")
            self.util.click_selector(self.login_team_selector)
        else:
            print("The Url is Error!")

    def trans_login(self):
        self.trans_selector = 'body > div.index-box > div > section.section-box.support.bg-gray > div > div:nth-child(1) > p > a > strong'
        self.login_button_selector = 'body > div.index-box > header > section > div.sign-in-group.pull-right.clearfix > a.trans-btn.size-m.pull-left'
        self.util.click_selector(self.login_button_selector)
        self.util.login_personal(u'15011554977', u'123456')
        if self.util.current_url() == 'https://transgod.cn':
            print("The Url is True!")
            self.util.click_selector(self.trans_selector)
        else:
            print("The Url is Error!")

    def trans_file_login(self):
        self.trans_file_selector = 'body > div.index-box > div > section.section-box.support.bg-gray > div > div:nth-child(2) > p > a > strong'
        self.login_button_selector = 'body > div.index-box > header > section > div.sign-in-group.pull-right.clearfix > a.trans-btn.size-m.pull-left'
        self.util.click_selector(self.login_button_selector)
        self.util.login_personal(u'15011554977', u'123456')
        if self.util.current_url() == 'https://transgod':
            print("The Url is True!")
            self.util.click_selector(self.trans_file_selector)
        else:
            print("The Url is Error!")






