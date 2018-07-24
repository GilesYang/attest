import unittest
import HTMLTestRunner
import os
from Units import index_unit, register_unit
# from Firefox_Utils import Email


class Report(object):
    def suit(self):
        self.suit = unittest.TestSuite()
        # 加入unittest单元测试类
        # self.suit.addTest(unittest.makeSuite(index_unit.IndexUnit))
        self.suit.addTest(unittest.makeSuite(register_unit.RegisterUnit))
        # 出报告
        self.files = os.getcwd()+"/Test_Report.html"
        self.filename = open(self.files, 'wb')
        self.runner = HTMLTestRunner.HTMLTestRunner(
            stream=self.filename,
            title=u"TransGod Personal Test Report",
            description="http://atman.ai/")
        self.runner.run(self.suit)

if __name__ == '__main__':
    R = Report()
    R.suit()
