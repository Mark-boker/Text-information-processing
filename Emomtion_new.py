# coding=utf-8
import csv
import re

import anls as anls
import numpy as np
import pandas as pd
import jieba
from collections import Counter



# 定义要处理的 CSV 文件路径
from matplotlib import pyplot as plt

file_path = r"C:\Users\Boker\PycharmProjects\Emotion analysis\test1.csv"
data = pd.read_csv(open(file_path, encoding='gbk', errors='ignore'))
# print(data.head())
data_title_emo = data[["情感倾向"]].copy().astype(str)  # 复制到新的地址，不破坏原始数据

newemo = data_title_emo.loc[0:10000, "情感倾向"]


print(data.情感倾向[0:10000].value_counts().sort_index(ascending=False))



b = Counter(newemo)
header = ['情感倾向', '数量']  # csv列名
with open('emo.csv', 'w', encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for key, value in dict(b).items():# 转换为字典
        writer.writerow([key, value])