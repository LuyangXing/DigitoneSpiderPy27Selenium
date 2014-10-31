#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'luyang'
__Email__ = 'Leon.LuyangXing@gmail.com'

# 排序程序测试
import operator
a = [['1','2'],['0','1'],['3','4'],['2','3']]
# 按0,1元素排序
b = sorted(a, key=operator.itemgetter(0,1))
print b