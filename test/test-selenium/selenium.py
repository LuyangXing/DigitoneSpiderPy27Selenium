#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'luyang'
__Email__ = 'Leon.LuyangXing@gmail.com'

from threading import Thread
from Queue import Queue
from time import sleep
from random import SystemRandom
import math
#q是任务队列
#NUM是并发线程总数
#JOBS是有多少任务
q = Queue()
NUM = 5
JOBS = 30
#具体的处理函数，负责处理单个任务
def do_somthing_using(arguments):
    print arguments
#这个是工作进程，负责不断从队列取数据并处理
def working():
    while True:
        arguments = q.get()
        do_somthing_using(arguments)
        x = math.ceil(10)
        print SystemRandom
        sleep(x)
        q.task_done()
#fork NUM个线程等待队列
for i in range(NUM):
    t = Thread(target=working)
    t.setDaemon(True)
    t.start()
#把JOBS排入队列
for i in range(JOBS):
    q.put(i)
#等待所有JOBS完成
q.join()
