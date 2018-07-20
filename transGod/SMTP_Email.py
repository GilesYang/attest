import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os


Exceptions = 'No Exception'
def send_email(smtpHost, sendAddress, password, receiveAddress, subject='', content=''):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddress
    msg['to'] = receiveAddress
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
    subject = 'python测试邮件'
    content = '一封来自QA的测试报告邮件'
    send_email('smtp.163.com', '15764512789@163.com', 'qwerqwer123456', 'yangjuntao@atman360.com', subject, content)
except Exception as error:
    print(error)
else:
    print(Exceptions)