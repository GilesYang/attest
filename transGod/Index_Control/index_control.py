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

