#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'luyang'
__Email__ = 'Leon.LuyangXing@gmail.com'

import threading
from time import sleep, ctime
import csv
from selenium import webdriver

try:
    driver = webdriver.Firefox()
    driver.get("http://item.jd.com/971501.html")
    # 产品名称、价格、产品编码
    elem1 = driver.find_element_by_xpath("//div/h1")
    elem2 = driver.find_element_by_id("jd-price")
    elem3 = driver.find_element_by_xpath("//li/div/span")
    a = elem1.text
    b = elem2.text
    c = elem3.text
    print
    print a
    print
    print b
    print
    print c
finally:
    driver.close()

reader = csv.reader(file('egg.csv', 'rb'))
for line in reader:
    #column=csvfile.readline().split(",")
    print
writer = csv.writer(open('egg2.csv', "wb"), dialect='excel', quoting=csv.QUOTE_ALL)
writer.writerow(["121", "121"])
writer.writerows([["121", "121"]])

loops = [4, 2]


def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'start loop', nloop, 'done at:', ctime()


def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print 'all done at:', ctime()

if __name__ == '__main__':
    main()