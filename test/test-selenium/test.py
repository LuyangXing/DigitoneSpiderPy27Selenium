#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'luyang'
__Email__ = 'Leon.LuyangXing@gmail.com'

# ====== Part I - about file ======
# 声明全局文件名
FILENAME = 'jd.csv'


def line_count(afilename):
    # 获取文件行数
    count = len(open(afilename, "rU").readlines())
    return count

N_FILENAME = line_count(FILENAME)
# ====== Part I - END ======

# ====== Part II - csv reader & writer ======
# 根据行数声明空白二维数组
multilist = [[0 for col in range(0)] for row in range(N_FILENAME)]

import csv


def csv_to_multilist(afilename):
    # 读取csv文件，生成二维数组内容
    reader = csv.reader(file(afilename, 'rb'))
    i = 0
    for line in reader:
        multilist[i] += line
        i += 1


def multilist_to_csv(afilename):
    # 将二维数组内容，写回文件中
    writer = csv.writer(open(afilename, "wb"), dialect='excel', quoting=csv.QUOTE_ALL)
    writer.writerows(multilist)
# ====== Part II - END ======

# ====== Part III - thread ======
import Queue
import threading
import time


class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1)
# ====== Part III - END ======

# ====== Part IV - selenium ======
# from selenium import webdriver
# def run_selenium():
#     driver = webdriver.Firefox()
#     driver.get("http://item.jd.com/971501.html")
#     # 产品名称、价格、产品编码
#     elem1 = driver.find_element_by_xpath("//div/h1")
#     elem2 = driver.find_element_by_id("jd-price")
#     elem3 = driver.find_element_by_xpath("//li/div/span")
#     a = elem1.text
#     b = elem2.text
#     c = elem3.text
#     driver.close()
# ====== Part IV - END ======

def main():
    # 执行读取动作
    csv_to_multilist(FILENAME)

    # 执行流程
    print "Starting Main Thread"
    global exitFlag
    exitFlag = 0
    threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5"]
    global queueLock
    queueLock = threading.Lock()
    global workQueue
    workQueue = Queue.Queue(N_FILENAME)
    threads = []
    threadID = 1
    # 创建新线程
    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1
    # 填充队列
    queueLock.acquire()
    for word in multilist:
        workQueue.put(word[0])
        #run_selenium()
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

    # 执行写入动作
    multilist_to_csv(FILENAME)

if __name__ == '__main__':
    main()