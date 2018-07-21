import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import datetime


Exceptions = 'No Exception'
def send_email(smtpHost, sendAddress, password, receiveAddress, subject='', content=''):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddress
    msg['to'] = ''.join(receiveAddresses)
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)


    file = os.getcwd()
    print(file)
    report_file = file+"/Suit/Test_Report.html"


    part = MIMEApplication(open(report_file, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename='Test_Report.html')
    msg.attach(part)

    smtp = smtplib.SMTP()
    smtp.connect(smtpHost, '25')
    smtp.login(sendAddress, password)
    smtp.sendmail(sendAddress, receiveAddress, str(msg))
    smtp.quit()
try:
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    subject = "Test_Report"
    content = '一封来自QA杨俊涛的测试报告邮件.'+'Report Time:'+now_time
    receiveAddresses = \
        [
            'yangjuntao@atman360.com',
            'zhanglibin@atman360.com',
            'liuwei@atman360.com',
            'zbwyn@126.com',
            'shaoshuai@atman360.com'
        ]
    send_email('smtp.163.com', '15764512789@163.com', 'qwerqwer123456', receiveAddresses, subject, content)
except Exception as error:
    print(error)
else:
    print(Exceptions)