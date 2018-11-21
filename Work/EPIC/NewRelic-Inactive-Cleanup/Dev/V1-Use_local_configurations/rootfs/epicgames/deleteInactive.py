#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: deleteInactive.py
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

import os
import time
import pycurl
import StringIO
import json
import sys
import certifi
import logging
from Queue import Queue

# import self-defined module
from getTotal import getTotalPage
from myUtils import *
from upload2S3 import upload_to_s3

q = Queue()

# logging Configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%a %d %b %Y %H:%M:%S',
                    filename='mylog',
                    filemode='w')

# Delete unactive server one by one
def traverseAndDelete(totalPage):
    num = 1
    for onePage in range(1, totalPage+1):
        url = 'https://api.newrelic.com/v2/servers.json?page='+str(onePage)
        data = curlGet(url)
        server_list = data['servers']
        for item in server_list:
            if not item['reporting']:
                global q
                q.put(item['id'])
                logging.info('Put '+str(item['id'])+':reporting='+str(item['reporting'])+' in the queue, number '+str(num)+'.')
                num = num+1

def serverDelete():
    global q
    logging.info('Going to delete unactive servers, queue size is ' + str(q.qsize()))
    for item in range(1, q.qsize()+1):
        qNumber = str(q.get())
        logging.info('Going to delete number ' + str(item) + ' unactive server, id is ' + qNumber)
        url = 'https://api.newrelic.com/v2/servers/'+qNumber+'.json'
        data = curlDelete(url)
        server_info = data['server']
        logging.info(str(server_info['id'])+" has been deleted.")
        #logging.info(url+" has been deleted")

def main():
    totalPage = getTotalPage()
    traverseAndDelete(int(totalPage))
    serverDelete()

    file = open('mylog', 'r+')
    currentDate = time.strftime("%Y%m%d")
    key = 'newrelic-cleanup-log_'+currentDate

    if upload_to_s3(file, key):
        print 'Upload '+key+' to AWS S3/newrelic-clean-up-log complete.'
    else:
        print 'Upload '+key+' to AWS S3/newrelic-clean-up-log failed.'

if __name__ == '__main__':
    main()