#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: upload2S3.py
#   Version: 0.1
#   Version: 0.2 use credentials injected via the environment
#   Author: Alan Tang
#   Date: 2016-11-28
#   Language: Python 2.7.12
#   Description: Upload file to AWS S3 using boto
#   Reference: http://stackabuse.com/example-upload-a-file-to-aws-s3/
#---------------------------------------

import os
import boto
from boto.s3.key import Key

aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
bucket_name = os.environ['BUCKET_NAME']
project_name = os.environ['PROJECT_NAME']
env_name = os.environ['ENV_NAME']

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

    # create a connection
    conn = boto.connect_s3(aws_access_key_id, aws_secret_access_key)
    # access a bucket
    bucket = conn.get_bucket(bucket_name, validate=True)
    # upload to a specific location
    full_key_name = os.path.join(env_name, key)
    k = Key(bucket)
    k.key = full_key_name
    # store data
    sent = k.set_contents_from_file(file, rewind=True)

    # Rewind for later use
    file.seek(0)

    if sent:
        return True
    return False

    # return 'size:'+str(size)+'sent:'+str(sent)

    # the sent should be equal to size if there is no folder
    # if sent == size:
    #     return True
    # return False

def main():

    file = open('myapp.log', 'r+')
    key = file.name

    print upload_to_s3(file, key)

    # if upload_to_s3(file, key):
    #     print 'It worked!'
    # else:
    #     print 'The upload failed...'

if __name__ == '__main__':
    main()