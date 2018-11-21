#coding: utf-8

import os,sys,time,subprocess
import warnings,logging

# 屏蔽scapy无用告警信息
warnings.filterwarnings("ignore", category=DeprecationWarning)
# 屏蔽模块IPv6多余告警
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import traceroute

# 接受输入的域名或IP
domains = raw_input("Please input one or more IP/domain: ")
target = domains.split(' ')
# 扫描的端口列表
dport = [80]

if len(target) >= 1 and target[0] != '':
    # 启动路由跟踪
    res,unans = traceroute(target,dport=dport,retry=-2)
    # 生成svg矢量图形
    res.graph(target="> test.svg")
    time.sleep(1)
    # svg转png格式
    subprocess.Popen("/usr/bin/convert test.svg test.png", shell=True)
else:
    print "IP/domain number of errors,exit"



