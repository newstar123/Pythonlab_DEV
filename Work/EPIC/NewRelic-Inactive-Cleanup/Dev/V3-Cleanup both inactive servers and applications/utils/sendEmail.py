#!/usr/bin/python

from email.mime.text import MIMEText
import smtplib

from logUtil import logUtil

class sendEmail(object):

    def __init__(self):
        self.log = logUtil('mylog')
        self.smtp_server = "email-smtp.us-east-1.amazonaws.com"
        self.smtp_port = '25'
        self.smtp_user = "xxxx"
        self.smtp_pass = "xxxx"
        self.fromaddr = "newrelic-inactive-handler@epicgames.com"

        server = smtplib.SMTP(
            host = self.smtp_server,
            port = self.smtp_port,
            timeout = 10
        )
        # server.set_debuglevel(10)
        server.starttls()
        server.ehlo()
        server.login(self.smtp_user, self.smtp_pass)
        self._server = server

    def sendTxtMail(self, to_list, mail_subject, mail_content, subtype='html'):

        msg = MIMEText(mail_content, _subtype=subtype, _charset='utf-8')
        msg['Subject'] = mail_subject
        msg['From'] = self.fromaddr
        # msg['To'] = ";".join(to_list)
        msg['To'] = ",".join(to_list)

        try:
            self._server.sendmail(self.fromaddr, to_list, msg.as_string())
            # return True
            # print "Message sent successfully"
            self.log.warn('Message sent successfully')
        except Exception, e:
            # print str(e)
            # return False
            # print "Message sent failed, Error: "+str(e)
            self.log.warn('Message sent failed, Error: '+str(e))

    def __del__(self):
        self._server.quit()
        self._server.close()

if __name__ == '__main__':

    mailto_list = ['alan.tang@epicgames.com']

    mail = sendEmail()

    if mail.sendTxtMail(mailto_list, "test mail", "hello world"):
        print "success"
    else:
        print "failed"