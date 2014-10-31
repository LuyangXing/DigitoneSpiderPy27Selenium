#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'luyang'
__Email__ = 'Leon.LuyangXing@gmail.com'

# ====== Part I - about file ======
# ====== Part II - csv reader & writer ======
# ====== Part III - Threads ======
#loops = [[1, 100001],[2, 100002],[3,100003],[4,100004],[5, 100005],[6, 100006],[7,100007],[8,100008],[9, 100009]]

import os
import threading
lock = threading.Lock()  # Lock (i.e., mutex)
import time


def doChore():
    time.sleep(0.2)

x = 88

def threader(tid):
    global x
    global lock
    while True:
        lock.acquire()  # Lock; or wait if other thread is holding the lock
        if x != 0:
            print 'running = %s' % x
            print tid
            x -= 1
            doChore()
        else:
            os._exit(0)
        lock.release()  # Unblock

for i in range(4):
    new_thread = threading.Thread(target=threader, args=(i,))
    # Set up thread; target: the callable (function) to be run, args: the argument for the callable
    new_thread.start()
