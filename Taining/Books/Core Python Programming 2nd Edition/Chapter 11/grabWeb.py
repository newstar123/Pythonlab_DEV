#!/usr/bin/env python
#coding:utf-8
#这段脚本下载了一个Web页面并显示了HTML文件的第一个以及最后一个非空格行。

from urllib import urlretrieve

def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine

def firstLast(webpage):
    f=open(webpage)
    lines=f.readlines()
    f.close()
    print firstNonBlank(lines),
    lines.reverse()
    print firstNonBlank(lines),

def download(url='http://www.yahoo.com', process=firstLast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:
        process(retval)

if __name__ == '__main__':
    #download()
    download('http://www.GOOGLE.com')

