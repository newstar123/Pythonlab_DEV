#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: logUtil.py
#   Version: 0.1
#   Author: Alan Tang
#   Date: 2016-12-12
#   Language: Python 2.7.12
#   Description: logging Utils
#   Reference: https://my.oschina.net/yangyanxing/blog/176933
#---------------------------------------

import os
import logging

class logUtil:

    def __init__(self, path, clevel=logging.WARNING, flevel=logging.INFO):
        self.logutil = logging.getLogger(path)
        self.logutil.setLevel(logging.INFO)
        fmt = logging.Formatter('%(asctime)s - %(message)s', '%Y-%m-%d %H:%M:%S')
        # 这里进行判断，如果handlers列表为空，则添加，否则，直接去写日志
        if not self.logutil.handlers:
            # 设置CMD日志
            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(clevel)
            # 设置文件日志
            fh = logging.FileHandler(path, mode='a')
            fh.setFormatter(fmt)
            fh.setLevel(flevel)

            self.logutil.addHandler(sh)
            self.logutil.addHandler(fh)

    def debug(self, message):
        self.logutil.debug(message)

    def info(self, message):
        self.logutil.info(message)

    def warn(self, message):
        self.logutil.warn(message)

    def error(self,message):
        self.logutil.error(message)

    def crit(self,message):
        self.logutil.critical(message)