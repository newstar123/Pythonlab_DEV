#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: storage.py
#   Version: 0.1
#   Author: Alan Tang
#   Date: 2016-12-08
#   Language: Python 2.7.12
#   Description: store buffer
#---------------------------------------

class Storage:
    def __init__(self):
        self.contents = ''

    def store(self, buf):
        self.contents = "%s%s" % (self.contents, buf)

    def __str__(self):
        return self.contents