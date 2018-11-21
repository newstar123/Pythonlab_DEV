# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：sendTextMail.py
#   版本：0.1
#   作者：ctang
#   日期：2016-03-03
#   语言：Python 2.7.10
#   说明：发送txt文本邮件
#   参考：http://www.cnblogs.com/xiaowuyi/archive/2012/03/17/2404015.html
#---------------------------------------

import smtplib
from email.mime.text import MIMEText

mailto_list = ["mchina_tang@qq.com"]
mail_host = "smtp.126.com"      #定义smtp主机
mail_user = "mchina_tang"       #用户名
mail_pass = "163@beijing0512"   #口令
mail_postfix = "126.com"        #发件箱的后缀

def sendMail(to_list, sub, content):
    me = mail_user+" <"+mail_user+"@"+mail_postfix+">"
    #创建一个MIMEText对象，分别指定HTML内容、类型（文本或html）、字符编码
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = sub    #邮件主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    try:
        server = smtplib.SMTP()     #创建一个SMTP()对象
        server.connect(mail_host)   #通过connect方法连接smtp主机
        server.login(mail_user+"@"+mail_postfix, mail_pass)     #邮箱账号登录校验
        server.sendmail(me, to_list, msg.as_string())           #邮件发送
        server.quit()   #断开smtp连接
        return True
    except Exception, e:
        print "失败" + str(e)
        return False

if __name__ == '__main__':
    if sendMail(mailto_list, "ask questions", "Test邮件"):
        print "邮件发送成功！"
    else:
        print "发送失败"

