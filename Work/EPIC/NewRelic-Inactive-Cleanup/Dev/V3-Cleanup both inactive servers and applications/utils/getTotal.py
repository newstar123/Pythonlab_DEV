#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: getTotal.py
#   Version: 0.2 Encapsulate into a function
#   Version: 0.3 Encapsulated into a class
#   Author: Alan Tang
#   Date: 2016-12-08
#   Language: Python 2.7.12
#   Description: Get the total page of applications and servers
#   API: https://docs.newrelic.com/docs/apis/rest-api-v2/requirements/pagination-api-output
#---------------------------------------

import re

from storage import Storage
from myUtils import myUtils


class getTotal:

    def __init__(self):
        self.retrieved_headers = Storage()
        self.myUtils = myUtils()
        self.app_url = 'https://api.newrelic.com/v2/applications.json'
        self.serv_url = 'https://api.newrelic.com/v2/servers.json'
        self.pattern = '.*next.*page=(.+)>;.*'

    def getAppTotalPage(self):
        result = self.myUtils.curlHeader(self.app_url)
        pattern_lastpage = re.compile(self.pattern, re.S)
        lastpage = re.search(pattern_lastpage, str(result))
        if lastpage:
            return lastpage.group(1)
        else:
            return 1

    def getServTotalPage(self):
        result = self.myUtils.curlHeader(self.serv_url)
        pattern_lastpage = re.compile(self.pattern, re.S)
        lastpage = re.search(pattern_lastpage, str(result))
        if lastpage:
            return lastpage.group(1)
        else:
            return 1

if __name__ == '__main__':
    gt = getTotal()
    print gt.getAppTotalPage()