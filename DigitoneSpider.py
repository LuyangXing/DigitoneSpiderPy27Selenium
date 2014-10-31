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
        x = get_products(urlcode=line[0])
        multilist[i].append(x[0])
        multilist[i].append(x[1])
        #multilist[i].append(x[2])
        i += 1
        print multilist


def multilist_to_csv(afilename):
    # 将二维数组内容，写回文件中
    writer = csv.writer(open(afilename, "wb"), dialect='excel', quoting=csv.QUOTE_ALL)
    writer.writerows(multilist)
# ====== Part II - END ======

# ====== Part III - Webdriver ======
from selenium import webdriver


def get_products(urlleft="http://item.jd.com/", urlcode="971501", urlright=".html"):
    try:
        driver = webdriver.Firefox()
        driver.get("%s%s%s" % (urlleft, urlcode, urlright))
        # 产品名称、价格、产品编码
        elem1 = driver.find_element_by_xpath("//div/h1")
        elem2 = driver.find_element_by_id("jd-price")
        #elem3 = driver.find_element_by_xpath("//li/div/span")
        return [elem1.text.encode('utf-8'), elem2.text.encode('utf-8')]
        #, (elem3.text).encode('utf-8')]

    finally:
        driver.close()
# ====== Part III - END ======

# ====== Part IV - Main ======


def main():
    csv_to_multilist(FILENAME)
    multilist_to_csv(FILENAME)
# ====== Part IV - END ======


if __name__ == '__main__':
    main()