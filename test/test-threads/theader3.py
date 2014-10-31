#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'luyang'
__Email__ = 'Leon.LuyangXing@gmail.com'

import Queue
import threading
import time

exitFlag = 0


class MyThread (threading.Thread):
    def __init__(self, threadid, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadid
        self.name = name
        self.q = q

    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name


def process_data(threadname, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadname, data)
        else:
            queueLock.release()
        time.sleep(5)

threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5"]
nameList = ["One-1", "Two-1", "Three-1", "Four-1", "Five-1", "One-2", "Two-2", "Three-2", "Four-2", "Five-2",
            "One-3", "Two-3", "Three-3", "Four-3", "Five-3", "One-4", "Two-4", "Three-4", "Four-4", "Five-4"]
queueLock = threading.Lock()
workQueue = Queue.Queue(20)
threads = []
threadID = 1

# 开始处理
print "Starting Main Thread"

# 创建新线程
for tName in threadList:
    thread = MyThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print "Exiting Main Thread"
