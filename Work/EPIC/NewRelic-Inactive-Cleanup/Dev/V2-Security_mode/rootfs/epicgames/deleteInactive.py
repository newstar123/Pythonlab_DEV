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
import pycurl
import StringIO
import json
import sys
import time
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

# log to file and print to stdout
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(message)s', '%Y-%m-%d %H:%M:%S')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# Put the inactive server id in a queue
def putInQueue(totalPage):
    num = 1
    for onePage in range(1, totalPage+1):
        url = 'https://api.newrelic.com/v2/servers.json?page='+str(onePage)
        data = curlGet(url)
        server_list = data['servers']
        for item in server_list:
            if not item['reporting']:
                global q
                q.put(item['id'])
                logging.info('Put id='+str(item['id'])+':name='+str(item['name'])+':reporting='+str(item['reporting'])+' in the queue, number '+str(num)+'.')
                num = num+1

def serverDelete():
    global q
    logging.info('Going to delete inactive servers, queue size is ' + str(q.qsize()))
    for item in range(1, q.qsize()+1):
        qNumber = str(q.get())
        logging.info('Going to delete number ' + str(item) + ' inactive server, id is ' + qNumber)
        url = 'https://api.newrelic.com/v2/servers/'+qNumber+'.json'
        # data = curlDelete(url)
        # server_info = data['server']
        # logging.info(str(server_info['id'])+':'+str(server_info['name'])+' has been deleted.')
        logging.warning(url+" has been deleted")

def main():
    totalPage = getTotalPage()
    putInQueue(int(totalPage))
    serverDelete()

    file = open('mylog', 'r+')
    currentDate = time.strftime("%Y%m%d")
    key = 'newrelic-cleanup-'+currentDate+'.log'

    # print upload_to_s3(file, key)

    if upload_to_s3(file, key):
        print 'Upload '+key+' to AWS S3:ops-cron-job-logs/newrelic-inactive-clean-up complete.'
    else:
        print 'Upload '+key+' to AWS S3:ops-cron-job-logs/newrelic-inactive-clean-up failed.'

if __name__ == '__main__':
    main()