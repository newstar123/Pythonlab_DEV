#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: upload2S3.py
#   Version: 0.1
#   Author: Alan Tang
#   Date: 2016-11-28
#   Language: Python 2.7.12
#   Description: Upload file to AWS S3 using boto
#   Reference: http://stackabuse.com/example-upload-a-file-to-aws-s3/
#---------------------------------------

import os
import boto
from boto.s3.key import Key
import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("epicgames.conf")
aws_access_key = cf.get('aws', 'aws_access_key')
aws_access_secret_key = cf.get('aws', 'aws_access_secret_key')
bucket_name = cf.get('aws', 'bucket')

def upload_to_s3(file, key):
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

    conn = boto.connect_s3(aws_access_key, aws_access_secret_key)
    bucket = conn.get_bucket(bucket_name, validate=True)
    k = Key(bucket)
    k.key = key
    sent = k.set_contents_from_file(file, rewind=True)

    # Rewind for later use
    file.seek(0)

    if sent == size:
        return True
    return False

def main():

    file = open('myapp.log', 'r+')
    key = file.name

    if upload_to_s3(file, key):
        print 'It worked!'
    else:
        print 'The upload failed...'

if __name__ == '__main__':
    main()