#!/usr/bin/env python
#coding: utf-8
#实现网卡流量图表绘制

import rrdtool
import time,psutil

total_input_traffic = psutil.net_io_counters()[1]
total_output_traffic = psutil.net_io_counters()[0]
starttime = int(time.time())
update = rrdtool.updatev('/root/AutomationOPS/rrdtool/Flow.rrd','%s:%s:%s' % (str(starttime),str(total_input_traffic),str(total_output_traffic)))
print update




