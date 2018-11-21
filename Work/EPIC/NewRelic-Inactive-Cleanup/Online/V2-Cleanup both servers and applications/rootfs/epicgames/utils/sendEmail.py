#!/usr/bin/python

import os
import smtplib
from email.mime.text import MIMEText

from logUtil import logUtil


class sendEmail(object):

    def __init__(self):
        self.log = logUtil('mylog')
        self.smtp_server = os.environ['SMTP_SERVER']
        self.smtp_port = os.environ['SMTP_PORT']
        self.smtp_user = os.environ['SMTP_USERNAME']
        self.smtp_pass = os.environ['SMTP_PASSWORD']
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
            self.log.warn('Message sent successfully')
        except Exception, e:
            self.log.warn('Message sent failed, Error: '+str(e))

    def __del__(self):
        self._server.quit()
        self._server.close()