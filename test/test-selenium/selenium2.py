#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.bool_stop = False

    def run(self):
        while not self.bool_stop:
            print('进程%s,于%s' % (self.name, time.asctime()))
            time.sleep(1)

    def stop(self):
        self.bool_stop = True


def main():
    th = []
    for i in xrange(10):
        th.append(MyThread('dir'))
        th[i].start()


if __name__ == '__main__':
    main()