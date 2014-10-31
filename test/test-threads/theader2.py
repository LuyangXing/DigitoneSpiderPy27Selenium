#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'luyang'
__Email__ = 'Leon.LuyangXing@gmail.com'

try:
    pass
except ValueError, e:
    pass
finally:
    pass

import threading
import time
import os


def dochore():  # This function could be any function to do other chores.
    time.sleep(0.5)


def booth(tid):  # Function for each thread
    global i
    global lock
    while True:
        lock.acquire()  # Lock; or wait if other thread is holding the lock
        if i != 0:
            i -= 1  # Sell tickets
            print(tid, ':now left:', i)  # Tickets left
            dochore()  # Other critical operations
        else:
            print("Thread_id", tid, " No more tickets")
            os._exit(0)  # Exit the whole process immediately
        lock.release()  # Unblock
        dochore()  # Non-critical operations

i = 100  # Start of the main function | Available ticket number
lock = threading.Lock()  # Lock (i.e., mutex)

for k in range(10):  # Start 10 threads
    new_thread = threading.Thread(target=booth, args=(k,))
    # Set up thread; target: the callable (function) to be run, args: the argument for the callable
    new_thread.start()  # run the thread
