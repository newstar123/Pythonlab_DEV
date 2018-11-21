#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: logging-demo2.py
#   Version: 0.1
#   Author: Alan Tang
#   Date: 2016-11-24
#   Language: Python 2.7.12
#   Description: Test logging module
#---------------------------------------

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

# 执行结果 myapp.log
# Thu, 01 Dec 2016 13:29:11 - logging-demo2.py:22 - root - This is info message
# Thu, 01 Dec 2016 13:29:12 - logging-demo2.py:23 - root - This is warning message
