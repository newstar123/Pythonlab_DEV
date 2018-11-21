# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：test_collection_deque.py
#   版本：0.1
#   作者：ctang
#   日期：2016-01-29
#   语言：Python 2.7.10
#   说明：使用collection.deque来高效的完成队列任务.
#---------------------------------------

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")   # Terry 入队
queue.append("Graham")  # Graham 入队
print queue.popleft()   # 队首元素出队
print queue.popleft()   # 队首元素出队
print queue             # 队列中剩下的元素