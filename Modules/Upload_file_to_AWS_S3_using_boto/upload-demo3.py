#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: upload-demo3.py
#   Version: 0.1 Test every module
#   Author: Alan Tang
#   Date: 2016-11-25
#   Language: Python 2.7.12
#   Description: Upload file to AWS S3 using boto
#   Reference: http://stackabuse.com/example-upload-a-file-to-aws-s3/
#---------------------------------------

import os
import boto
from boto.s3.key import Key

def upload_to_s3(aws_access_key_id, aws_secret_access_key, file, bucket, key):
    """
    Uploads the given file to the AWS S3 bucket and key specified.

    Returns boolean indicating success/failure of upload.
    """
    try:
        size = os.fstat(file.fileno()).st_size
    except:
        # Not all file objects implement fileno(),
        # so we fall back on this
        file.seek(0, os.SEEK_END)
        size = file.tell()

    conn = boto.connect_s3(aws_access_key_id, aws_secret_access_key)
    bucket = conn.get_bucket(bucket, validate=True)
    k = Key(bucket)
    k.key = key
    sent = k.set_contents_from_file(file, rewind=True)

    # Rewind for later use
    file.seek(0)

    if sent == size:
        return True
    return False

# Using the code
AWS_ACCESS_KEY = 'xxxx'
AWS_ACCESS_SECRET_KEY = 'xxxx'

file = open('myapp.log', 'r+')
bucket = 'ops-log'

key = file.name

if upload_to_s3(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, file, bucket, key):
    print 'It worked!'
else:
    print 'The upload failed...'