#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: deleteServ.py
#   Version: 0.1 OOP
#   Author: Alan Tang
#   Date: 2016-12-08
#   Language: Python 2.7.12
#   Description: Delete inactive newrelic servers and applications
#---------------------------------------

import time

from utils.s3util import s3util
from handleApp import appClass
from handleServ import servClass

if __name__ == '__main__':

    # delete Servers
    sc = servClass()
    sc.handleServ()

    # delete Applications
    ac = appClass()
    ac.handleApp()

    # get the log info
    file = open('mylog', 'r+')
    currentDate = time.strftime("%Y%m%d")
    key = 'newrelic-cleanup-'+currentDate+'.log'

    # upload log to AWS S3
    su = s3util()
    su.upload_to_s3(file, key)
