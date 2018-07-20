import unittest
import HTMLTestRunner
import os
from Units import index_unit
# from Firefox_Utils import Email



# suit
suit = unittest.TestSuite()
# 加入unittest单元测试类
# suit.addTest(unittest.makeSuite(Register_Unit.RegisterUnit))
# suit.addTest(unittest.makeSuite(Login_Unit.LoginUnit))
# suit.addTest(unittest.makeSuite(ForgetPassword_Unit.ForgetPasswordUnit))
# suit.addTest(unittest.makeSuite(CreateProject_Unit.CreateProjectUnit))
# suit.addTest(unittest.makeSuite(TransgodInfoUnit.TransgodInfoUnit))
suit.addTest(unittest.makeSuite(index_unit.IndexUnit))
# 出报告
files = os.getcwd() +"/TransGodTest.html"
filename = open(files, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=filename, title=u"TransGod Personal Test Report", description="Selenium Case v2.0")
runner.run(suit)
