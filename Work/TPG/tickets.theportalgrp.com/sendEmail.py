# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：sendEmail.py
#   版本：0.1
#   作者：ctang
#   日期：2016-03-03
#   语言：Python 2.7.10
#   说明：发送邮件的模块类
#   参考：http://my.oschina.net/cloudcoder/blog/200272
#---------------------------------------

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class SendEmail(object):
    #构造函数：初始化基本信息
    def __init__(self, host, user, passwd):
        info = user.split("@")
        self._user = user
        self._account = info[0]
        self._me = self._account + " <" + self._user + ">"

        server = smtplib.SMTP()
        server.connect(host)
        server.login(self._user, passwd)
        self._server = server

    #发送文本或html邮件
    def sendTxtMail(self, to_list, sub, content, subtype='html'):
        # 如果发送的是文本邮件，则_subtype设置为plain
        # 如果发送的是html邮件，则_subtype设置为html
        msg = MIMEText(content, _subtype=subtype, _charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = self._me
        msg['To'] = ";".join(to_list)

        try:
            self._server.sendmail(self._me, to_list, msg.as_string())
            return True
        except Exception, e:
            print str(e)
            return False

    #析构函数，释放资源
    def __del__(self):
        self._server.quit()
        self._server.close()

if __name__ == '__main__':
    mailto_list = ['mchina_tang@qq.com']
    mail_host = "smtp.126.com"      #定义smtp主机
    mail_user = "mchina_tang@126.com"       #用户名
    mail_pass = "xxxx"   #口令

    mail = SendEmail(mail_host, mail_user, mail_pass)

    if mail.sendTxtMail(mailto_list, "测试邮件", "hello world！<br><br><p>你好，发送文本文件测试</p>"):
        print "邮件发送成功！"
    else:
        print "发送失败！"





