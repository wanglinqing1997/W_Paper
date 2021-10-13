# 在时序数据中实现多尺度部分周期模式增量挖掘
DataSets:数据集  
OutPut：输出结果  
Multi-Scale Incremental Partial Periodic Frequent Pattern——MSI-PPPGrowth

## 1. [division_csv.py](division_original_data.py)
把数据集分割成多个尺度（本程序暂定分割成10份，可自行修改。）

## 2.[abstract.py](abstract.py)
各种辅助函数

## 3.[threePGrowth.py](threePGrowth.py)
    threeP: partial periodic frequent pattern 
    3P-Growth算法
本论文主要算法，用于各个尺度件的挖掘。

## 4.[Incremental_Mining.py](Incremental_Mining.py)
增量挖掘算法