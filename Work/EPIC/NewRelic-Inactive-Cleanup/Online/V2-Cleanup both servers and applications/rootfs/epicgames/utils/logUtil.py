#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: logUtil.py
#   Version: 0.1
#   Author: Alan Tang
#   Date: 2016-12-12
#   Language: Python 2.7.12
#   Description: logging Utils
#---------------------------------------

import os
import logging

class logUtil:

    def __init__(self, path, clevel=logging.WARNING, flevel=logging.INFO):
        self.logutil = logging.getLogger(path)
        self.logutil.setLevel(logging.INFO)
        fmt = logging.Formatter('%(asctime)s - %(message)s', '%Y-%m-%d %H:%M:%S')

        if not self.logutil.handlers:
            # CMD log
            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(clevel)
            # file log
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