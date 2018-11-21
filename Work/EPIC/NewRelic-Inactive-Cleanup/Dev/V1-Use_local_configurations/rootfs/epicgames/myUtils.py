#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: myUtils.py
#   Version: 0.1
#   Author: Alan Tang
#   Date: 2016-11-23
#   Language: Python 2.7.12
#   Description: General utils
#---------------------------------------

import pycurl
import StringIO
import json
import sys
import certifi
import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("epicgames.conf")
header = cf.get('info', 'header')

def curlGet(url_address):
    c = pycurl.Curl()
    s = StringIO.StringIO()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(pycurl.URL, url_address)
    c.setopt(pycurl.WRITEFUNCTION, s.write)
    # c.setopt(pycurl.HTTPHEADER, ["X-Api-Key:xxxx"])
    c.setopt(pycurl.HTTPHEADER, ['X-Api-Key:'+header])
    c.perform()
    content = s.getvalue()
    json_data = json.loads(content)
    return json_data
    s.close()
    c.close()

def curlDelete(url_address):
    c = pycurl.Curl()
    s = StringIO.StringIO()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(pycurl.URL, url_address)
    c.setopt(pycurl.CUSTOMREQUEST, "DELETE")
    c.setopt(pycurl.WRITEFUNCTION, s.write)
    c.setopt(pycurl.HTTPHEADER, ["X-Api-Key:"+header])
    c.perform()
    content = s.getvalue()
    json_data = json.loads(content)
    return json_data
    s.close()
    c.close()

def main():
    pass

if __name__ == '__main__':
    main()