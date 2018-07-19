import unittest
from Units import Login_Unit
from Units import Register_Unit
from Units import ForgetPassword_Unit
from Units import CreateProject_Unit
from Units import TransgodInfoUnit
import HTMLTestRunner
import os
# from Firefox_Utils import Email



# suit
suit = unittest.TestSuite()
# 加入unittest单元测试类
suit.addTest(unittest.makeSuite(Register_Unit.RegisterUnit))
suit.addTest(unittest.makeSuite(Login_Unit.LoginUnit))
suit.addTest(unittest.makeSuite(ForgetPassword_Unit.ForgetPasswordUnit))
suit.addTest(unittest.makeSuite(CreateProject_Unit.CreateProjectUnit))
suit.addTest(unittest.makeSuite(TransgodInfoUnit.TransgodInfoUnit))
# 出报告
files = os.getcwd() +"/TransGodTest.html"
filename = open(files, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=filename, title=u"transgod", description="testcase", retry=1)
runner.run(suit)
