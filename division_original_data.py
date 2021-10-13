import datetime
import time
import csv
import os

start_time = datetime.datetime.now()
print('开始分割数据文件.')
print('*-*-' * 30 )
path = '//Datasets/T10I4D100K.csv'
#T10I4D100K.csv 有10万行数据
with open(path, 'r', newline='') as file:
    csvreader = csv.reader(file)
    #a = next(csvreader)
    #print(a)
    i = j = 0
    for row in csvreader:
        # print(row)
        # print(f'i is {i}',f'j is {j}')
        if i % 10000 == 0:
        #将CSV分割成10份
            j += 1
            print(f'T10I4D100K_Part_{j}.txt  生成成功')
            time.sleep(0.2)
        csv_path = os.path.join('//Datasets', 'T10I4D100K_Part_{}.txt'.format(j))
        # print(csv_path)
        if not os.path.exists(os.path.dirname(csv_path)):
            os.makedirs(os.path.dirname(csv_path))
            with open(csv_path, 'w', newline='') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(row)
            i += 1
        else:
            with open(csv_path, 'a', newline='') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(row)
            i += 1
end_time = datetime.datetime.now()
print('*-*-' * 30 )
print('分割结束,耗时{}.'.format(end_time - start_time))