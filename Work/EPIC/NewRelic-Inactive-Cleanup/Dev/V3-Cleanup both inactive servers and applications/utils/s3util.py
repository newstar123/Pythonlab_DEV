#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: myBoto.py
#   Version: 0.1
#   Version: 0.2 use credentials injected via the environment
#   Author: Alan Tang
#   Date: 2016-12-01
#   Language: Python 2.7.12
#   Description: Upload file to AWS S3 using boto
#   Reference: http://stackabuse.com/example-upload-a-file-to-aws-s3/
#---------------------------------------

import os
import boto
from boto.s3.key import Key
from logUtil import logUtil

class s3util:

    def __init__(self):
        self.log = logUtil('mylog')
        # self.aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
        # self.aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
        # self.bucket_name = os.environ['BUCKET_NAME']
        # self.project_name = os.environ['PROJECT_NAME']
        # self.env_name = os.environ['ENV_NAME']

        self.aws_access_key_id = 'xxxx'
        self.aws_secret_access_key = 'xxxx'
        self.bucket_name = 'xxxx'
        self.project_name = 'newrelic-inactive-clean-up'
        self.env_name = 'Dev'
        self.s3_full_path = os.path.join(self.bucket_name, self.project_name, self.env_name)

    def download_s3(self, filename):
        conn = boto.connect_s3(self.aws_access_key_id, self.aws_secret_access_key)
        bucket = conn.get_bucket(self.bucket_name, validate=True)
        full_key_name = os.path.join(self.project_name, self.env_name, filename)
        k = Key(bucket)
        k.key = full_key_name
        try:
            k.get_contents_to_filename(filename)
        except Exception, e:
            # print 'File does not exist, download failed.'
            self.log.warn('File inactivelist.txt does not exist on AWS S3.')

    def upload_to_s3(self, file, key):
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
        conn = boto.connect_s3(self.aws_access_key_id, self.aws_secret_access_key)
        # access a bucket
        bucket = conn.get_bucket(self.bucket_name, validate=True)
        # upload to a specific location
        full_key_name = os.path.join(self.project_name, self.env_name, key)
        k = Key(bucket)
        k.key = full_key_name
        # store data
        sent = k.set_contents_from_file(file, rewind=True)

        # Rewind for later use
        file.seek(0)

        if sent:
            # print 'Upload '+ key + ' to AWS S3:'+self.s3_full_path+' complete.'
            self.log.warn('Upload '+ key + ' to AWS S3:'+self.s3_full_path+' complete.')
        else:
            # print 'Upload '+ key + ' to AWS S3:'+self.s3_full_path+' failed.'
            self.log.warn('Upload '+ key + ' to AWS S3:'+self.s3_full_path+' failed.')

if __name__ == '__main__':

    su = s3util()

    # upload
    # file = open('mylog', 'r+')
    # key = 'newrelic-cleanup.log'
    # su.upload_to_s3(file, key)

    # download
    su.download_s3('inactivelist.txt')
