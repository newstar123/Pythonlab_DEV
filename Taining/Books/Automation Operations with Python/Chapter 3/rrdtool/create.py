#!/usr/bin/env python
#coding: utf-8
#实现网卡流量图表绘制

import rrdtool
import time

current_time = str(int(time.time()))
rrd = rrdtool.create('Flow.rrd', '--step', '300', '--start', current_time,
                     'DS:eth0_in:COUNTER:600:0:U',
                     'DS:eth0_out:COUNTER:600:0:U',
                     'RRA:AVERAGE:0.5:1:600',
                     'RRA:AVERAGE:0.5:6:700',
                     'RRA:AVERAGE:0.5:24:775',
                     'RRA:AVERAGE:0.5:288:797',
                     'RRA:MAX:0.5:1:600',
                     'RRA:MAX:0.5:6:700',
                     'RRA:MAX:0.5:24:775',
                     'RRA:MAX:0.5:444:797',
                     'RRA:MIN:0.5:1:600',
                     'RRA:MIN:0.5:6:700',
                     'RRA:MIN:0.5:24:775',
                     'RRA:MIN:0.5:444:797')
if rrd:
    print rrdtool.error()

