#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'luyang'
__Email__ = 'Leon.LuyangXing@gmail.com'

# ====== Part I - about file ======
# ====== Part II - csv reader & writer ======
# ====== Part III - Threads ======
#loops = [[1, 100001],[2, 100002],[3,100003],[4,100004],[5, 100005],[6, 100006],[7,100007],[8,100008],[9, 100009]]

import threading
import time
import os

# # This function could be any function to do other chores.
# def doChore():
#     time.sleep(0.5)

# Function for each thread
def booth(tid):
    # global i
    global lock
    while True:
        lock.acquire()                # Lock; or wait if other thread is holding the lock
        # if i != 0:
        #     i = i - 1                 # Sell tickets
        #     print(tid,':now left:',i) # Tickets left
        #     doChore()                 # Other critical operations
        # else:
        #     print
        #     # print("Thread_id",tid," No more tickets")
        #     os._exit(0)              # Exit the whole process immediately
        lock.release()               # Unblock
        # doChore()                    # Non-critical operations

# Start of the main function
# i    = 100                           # Available ticket number
lock = threading.Lock()              # Lock (i.e., mutex)

# Start 10 threads
for k in range(10):
    new_thread = threading.Thread(target=booth,args=(k,))   # Set up thread; target: the callable (function) to be run, args: the argument for the callable
    new_thread.start()                                      # run the thread