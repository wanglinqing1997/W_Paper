import datetime
import time
import os

def getRunTime():
    '''
    返回程序运行时间
    '''
    costTime = endTime - startTime
    print('消耗时间{}'.format(costTime))
    return costTime

startTime = datetime.datetime.now()
for i in range(1, 11):
    path1 = '/Users/wanglinqing/PycharmProjects/111/Original_Output/patterns_dist_{}.txt'.format(i)
    # path1表示原数据路径
    path2 = '/Users/wanglinqing/PycharmProjects/111/Datasets/mergeData.txt'
    # path2表示合并数据后的新文件（mergeData）路径
    with open(path1, 'r') as file1, open(path2, 'a') as file2:
        for row in file1:
            file2.writelines(row)
        print('patterns_dist_{}.txt写入完毕'.format(i))
        time.sleep(0.5)
endTime = datetime.datetime.now()
getRunTime()




