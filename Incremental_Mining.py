# from abstract import *
# from threePGrowth import *
import csv
import os
import datetime
import time
import sys

'''
读取Original_OutPut中的数据
'''
start_time = datetime.datetime.now()
for i in range (1, 11):
    k = '/Users/wanglinqing/PycharmProjects/W_Paper/Datasets/T10I4D100K_Part_{}.txt'.format(i)
    j = 0
    with open(k, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            j += 1
            print(row)
    print('T10I4D100K_Part_{}.txt 输出完毕 一共输出{}行'.format(i, j))
    time.sleep(1)
end_time = datetime.datetime.now()
print('消耗时间{}'.format(end_time - start_time))

