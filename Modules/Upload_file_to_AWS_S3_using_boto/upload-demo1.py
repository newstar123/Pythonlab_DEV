#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: upload-demo1.py
#   Version: 0.1 Test every module
#   Author: Alan Tang
#   Date: 2016-11-25
#   Language: Python 2.7.12
#   Description: Upload file to AWS S3 using boto
#---------------------------------------

from boto.s3.connection import S3Connection
from boto.s3.key import Key

conn = S3Connection('xxxx', 'xxxx')

b = conn.get_bucket('ops-log')
k = Key(b)
k.key = 'myfile'
k.set_contents_from_filename('myapp.log')