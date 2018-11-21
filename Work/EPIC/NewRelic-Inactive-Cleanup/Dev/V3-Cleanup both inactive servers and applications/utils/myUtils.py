#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: myUtils.py
#   Version: 0.1
#   Author: Alan Tang
#   Date: 2016-11-30
#   Language: Python 2.7.12
#   Description: General utils
#---------------------------------------

import StringIO
import json
import os
import pycurl
import time

import certifi

from storage import Storage


class myUtils:

    def __init__(self):
        self.retrieved_headers = Storage()
        self.header = 'xxxx'

    def curlHeader(self, url):
        c = pycurl.Curl()
        s = StringIO.StringIO()
        c.setopt(pycurl.CAINFO, certifi.where())
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.HEADER, True)
        c.setopt(pycurl.HEADERFUNCTION, self.retrieved_headers.store)
        c.setopt(pycurl.WRITEFUNCTION, s.write)
        c.setopt(pycurl.HTTPHEADER, ['X-Api-Key:' + self.header])
        c.perform()
        return self.retrieved_headers
        s.close()
        c.close()

    def curlGet(self, url):
        c = pycurl.Curl()
        s = StringIO.StringIO()
        c.setopt(pycurl.CAINFO, certifi.where())
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.WRITEFUNCTION, s.write)
        c.setopt(pycurl.HTTPHEADER, ['X-Api-Key:' + self.header])
        c.perform()
        content = s.getvalue()
        json_data = json.loads(content)
        return json_data
        s.close()
        c.close()

    def curlDelete(self, url):
        c = pycurl.Curl()
        s = StringIO.StringIO()
        c.setopt(pycurl.CAINFO, certifi.where())
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.CUSTOMREQUEST, "DELETE")
        c.setopt(pycurl.WRITEFUNCTION, s.write)
        c.setopt(pycurl.HTTPHEADER, ["X-Api-Key:" + self.header])
        c.perform()
        content = s.getvalue()
        json_data = json.loads(content)
        return json_data
        s.close()
        c.close()

    def timeLimitExceeded(self, last_reported):
        last_reported_timestamp = time.mktime(time.strptime(last_reported, '%Y-%m-%dT%H:%M:%S+00:00'))
        current_timestamp = time.time()
        time_diff = current_timestamp - last_reported_timestamp

        # 3 days
        retention_time = 3600 * 24 * 3

        if time_diff > retention_time:
            return True
        else:
            return False

    def isFileEmpty(self, file):
        try:
            size = os.fstat(file.fileno()).st_size
        except:
            # Not all file objects implement fileno(),
            # so we fall back on this
            file.seek(0, os.SEEK_END)
            size = file.tell()

        if size == 0:
            return True
        else:
            return False