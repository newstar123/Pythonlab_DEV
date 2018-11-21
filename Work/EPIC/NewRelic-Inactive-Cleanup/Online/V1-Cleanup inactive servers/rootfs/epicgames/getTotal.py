#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: getTotal.py
#   Version: 0.2 Encapsulate into a function
#   Author: Alan Tang
#   Date: 2016-11-15
#   Language: Python 2.7.12
#   Description: Get the total page of server lists
#   API: https://docs.newrelic.com/docs/apis/rest-api-v2/requirements/pagination-api-output
#---------------------------------------

import os
import pycurl
import StringIO
import json
import sys
import certifi
import re

header = os.environ['NEWRELIC_API_KEY']

class Storage:
    def __init__(self):
        self.contents = ''

    def store(self, buf):
        self.contents = "%s%s" % (self.contents, buf)

    def __str__(self):
        return self.contents

retrieved_headers = Storage()

# Get the total page
def getTotalPage():
    url = 'https://api.newrelic.com/v2/servers.json'
    c = pycurl.Curl()
    s = StringIO.StringIO()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.HEADER, True)
    c.setopt(pycurl.HEADERFUNCTION, retrieved_headers.store)
    c.setopt(pycurl.WRITEFUNCTION, s.write)
    c.setopt(pycurl.HTTPHEADER, ['X-Api-Key:'+header])
    c.perform()

    pattern_lastpage = re.compile('.*next.*page=(.+)>;.*', re.S)
    lastpage = re.search(pattern_lastpage, str(retrieved_headers))

    s.close()
    c.close()

    return lastpage.group(1)
