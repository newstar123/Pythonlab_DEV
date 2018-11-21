#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: deleteServ.py
#   Version: 0.1 Test every module
#   Version: 0.2 Encapsulate into functions
#   Version: 0.3 Remove unnecessary items
#   Version: 0.4 Use queue
#   Author: Alan Tang
#   Date: 2016-11-15
#   Language: Python 2.7.12
#   Description: Delete inactive newrelic servers
#   API: https://rpm.newrelic.com/api/explore/servers/delete
#---------------------------------------

from Queue import Queue

from utils.getTotal import getTotal
from utils.logUtil import logUtil
from utils.myUtils import myUtils

class servClass:

    def __init__(self):
        self.q = Queue()
        self.myUtils = myUtils()
        self.log = logUtil('mylog')
        self.qUrl = 'https://api.newrelic.com/v2/servers.json?page='
        self.servBasicUrl = 'https://api.newrelic.com/v2/servers/'

    # Put the inactive server id in a queue
    def putInQueue(self, totalPage):
        num = 1
        self.log.warn('#################### Delete Inactive Servers ####################')
        self.log.warn('Putting inactive server id in a queue.')
        for onePage in range(1, totalPage+1):
            url = self.qUrl+str(onePage)
            data = self.myUtils.curlGet(url)
            server_list = data['servers']
            for item in server_list:
                if not item['reporting'] and self.myUtils.timeLimitExceeded(item['last_reported_at']):
                    self.q.put(item['id'])
                    self.log.info('Put id='+str(item['id'])+':name='+str(item['name'])+':reporting='+str(item['reporting'])+':last_reported_at='+str(item['last_reported_at'])+' in the queue, number '+str(num)+'.')
                    num = num+1

    def makeDelete(self):
        self.log.warn('Going to delete inactive servers, queue size is ' + str(self.q.qsize()))
        for item in range(1, self.q.qsize()+1):
            qNumber = str(self.q.get())
            self.log.info('Going to delete number ' + str(item) + ' inactive server, id is ' + qNumber)
            url = self.servBasicUrl+qNumber+'.json'
            data = self.myUtils.curlDelete(url)
            server_info = data['server']
            self.log.warn(str(server_info['id'])+':'+str(server_info['name'])+' has been deleted.')

        self.log.warn('Deleting completed.')

    def handleServ(self):
        gt = getTotal()
        totalPage = gt.getServTotalPage()
        self.putInQueue(int(totalPage))
        self.makeDelete()

if __name__ == '__main__':
    serv = servClass()
    serv.handleServ()