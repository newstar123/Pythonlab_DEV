#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: logging-demo1.py
#   Version: 0.1
#   Author: Alan Tang
#   Date: 2016-11-24
#   Language: Python 2.7.12
#   Description: Test logging module
#---------------------------------------

import logging

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

# 执行结果
# WARNING:root:This is warning message

# 说明
# 默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
# 日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。