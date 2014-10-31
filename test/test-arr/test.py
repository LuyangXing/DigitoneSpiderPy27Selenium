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
# 根据行数声明空白二维数组
multilist = [[0 for col in range(0)] for row in range(line_count(FILENAME))]


# ====== Part II - csv reader & writer ======
import csv


def csv_to_multilist(afilename):
    # 读取csv文件，生成二维数组内容
    reader = csv.reader(file(afilename, 'rb'))
    i = 0
    for line in reader:
        multilist[i] += line
        i += 1
# 执行读取动作
csv_to_multilist(FILENAME)
multilist[1] += ['a', 'b', 'c']


def multilist_to_csv(afilename):
    # 将二维数组内容，写回文件中
    writer = csv.writer(open(afilename, "wb"), dialect='excel', quoting=csv.QUOTE_ALL)
    writer.writerows(multilist)
# 执行写入动作
multilist_to_csv(FILENAME)