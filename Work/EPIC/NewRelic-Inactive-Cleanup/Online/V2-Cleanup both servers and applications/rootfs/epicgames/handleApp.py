#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: deleteApp.py
#   Version: 0.1 Test every module
#   Version: 0.2 Encapsulate into functions
#   Version: 0.3 Remove unnecessary items
#   Version: 0.4 Use queue
#   Version: 0.5 OOP
#   Version: 0.6 Intersection
#   Author: Alan Tang
#   Date: 2016-12-08
#   Language: Python 2.7.12
#   Description: Delete inactive newrelic applications
#   API: https://rpm.newrelic.com/api/explore/applications/delete
#---------------------------------------

import os
from Queue import Queue

from utils.getTotal import getTotal
from utils.sendEmail import sendEmail
from utils.logUtil import logUtil
from utils.myUtils import myUtils
from utils.s3util import s3util


class appClass:

    def __init__(self):
        self.q = Queue()
        self.myUtils = myUtils()
        self.mail = sendEmail()
        self.gt = getTotal()
        self.su = s3util()
        self.log = logUtil('mylog')
        self.num = 1
        self.qUrl = 'https://api.newrelic.com/v2/applications.json?page='
        self.appBasicUrl = 'https://api.newrelic.com/v2/applications/'
        self.tmp_content = 'Below applications in NewRelic stopped reporting, please take a look.<br><br>If no action taken in three days, these applications will be deleted.<br><br>'

    def makeDelete(self):
        self.log.warn('Going to delete inactive applications, queue size is ' + str(self.q.qsize()))
        for item in range(1, self.q.qsize()+1):
            qNumber = str(self.q.get())
            self.log.info('Going to delete number ' + str(item) + ' inactive application, id is ' + qNumber)
            url = self.appBasicUrl+qNumber+'.json'
            try:
                data = self.myUtils.curlDelete(url)
                application_info = data['application']
                self.log.warn(str(application_info['id'])+':'+str(application_info['name'])+' has been deleted.')
            except Exception, e:
                self.log.warn('Delete '+qNumber+' failed.')

        self.log.warn('Deleting completed.')

    def collectInactive(self, totalPage):
        # write the inactive app to a local file
        f = open('inactivelist.txt', 'w')
        self.log.warn('List lastest inactive applications to inactivelist.txt')
        for onePage in range(1, totalPage+1):
            url = self.qUrl+str(onePage)
            data = self.myUtils.curlGet(url)
            application_list = data['applications']
            for item in application_list:
                if not item['reporting']:
                    f.write(str(item['id'])+'\n')
                    self.tmp_content = self.tmp_content+str(self.num)+'. '+str(item['name'])+'<br>'
                    self.log.info(str(self.num) + '. '+'id=' + str(item['id']) + ':name=' + str(item['name']) + ':reporting=' + str(item['reporting']))
                    self.num = self.num+1
        f.close()

        self.log.warn("Total inactive applications: "+str(self.num-1))

        # upload to AWS S3
        su = s3util()
        file = open('inactivelist.txt', 'r+')
        key = 'inactivelist.txt'
        su.upload_to_s3(file, key)
        file.close()

    def collectInactiveToList(self, totalPage):
        ret_list = []
        for onePage in range(1, totalPage + 1):
            url = self.qUrl + str(onePage)
            data = self.myUtils.curlGet(url)
            application_list = data['applications']
            for item in application_list:
                if not item['reporting']:
                    ret_list.append(item['id'])

        return ret_list

    def sendNotification(self):
        # mailto_list = ['online-operations-aws-notices@epicgames.com', 'alan.tang@epicgames.com']
        mailto_list = ['alan.tang@epicgames.com']
        mail_subject = "NewRelic Inactive Applications - "+os.environ['ENV_NAME']
        mail_content = self.tmp_content
        self.mail.sendTxtMail(mailto_list, mail_subject, mail_content)

    def lineToList(self, file):
        # create a new list
        ret_list = []
        for line in file:
            ret_list.append(int(line.strip()))

        return ret_list

    def handleApp(self):
        self.log.warn('#################### Delete Inactive Applications ####################')
        self.log.warn('Tring to download inactivelist.txt from AWS S3')
        self.su.download_s3('inactivelist.txt')
        if os.path.exists('inactivelist.txt'):
            self.log.warn('Found inactive application list, going to delete them.')
            f = open('inactivelist.txt', 'r')
            last_list = self.lineToList(f)
            self.log.warn('Last list length: ' + str(len(last_list)))

            # get current
            totalPage = self.gt.getAppTotalPage()
            current_list = self.collectInactiveToList(int(totalPage))
            self.log.warn('Current list length: ' + str(len(current_list)))

            # The intersection of two lists
            intersection_list = [val for val in last_list if val in current_list]
            self.log.warn('Intersection list length: ' + str(len(intersection_list)))
            if intersection_list:
                for id in intersection_list:
                    self.q.put(id)
                # To delete
                self.makeDelete()
            else:
                self.log.warn('Last list and current list have no intersection.')
        else:
            self.log.warn('This is the first time to perform delete inactive applications.')

        # get the latest inactive app list
        totalPage = self.gt.getAppTotalPage()
        self.collectInactive(int(totalPage))
        if int(self.num-1) != 0:
            self.sendNotification()

if __name__ == '__main__':

    app = appClass()
    app.handleApp()