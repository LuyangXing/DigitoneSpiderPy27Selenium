#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

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

driver.close()





# import csv
#
# #从文件读取
# reader = csv.reader(file('egg.csv','rb'))
# for line in reader:
#     print line
#
# #写入文件
# writer = csv.writer(open('egg2.csv',"wb"),dialect='excel',quoting=csv.QUOTE_ALL)
# #传入list
# writer.writerow(["121","121"])
# #传入2纬list
# writer.writerows([["121","121"]])





# import threading
#
# from time import sleep,ctime
#
# loops=[10,2]
#
# def loop(nloop,nsec):
#
#        print 'start loop',nloop,'at:',ctime()
#        sleep(nsec)
#        print 'loop',nloop,'done at:',ctime()
#
# def main():
#
#        print 'starting at:',ctime()
#        threads=[]
#        nloops=range(len(loops))
#
#        for i in nloops:
#               t=threading.Thread(target=loop,args=(i,loops[i]))
#               threads.append(t)
#
#        for i in nloops:
#               threads[i].start()
#
#        for i in nloops:
#               threads[i].join()
#
#        print 'all done at:',ctime()
#
# if __name__=='__main__':
#        main()
