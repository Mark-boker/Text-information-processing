import csv
import re

import anls as anls
import numpy as np
import pandas as pd
import jieba
from collections import Counter

# 打开 CSV 文件，并读取数据
# with open(file_path, "r", encoding='gb18030') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)  # 跳过表头
#     data = [row for row in reader]
# # print(data)
# # 定义要去除的停用词列表
from PIL.Image import Image
from _tkinter import _flatten
from matplotlib import pyplot as plt
from nltk.corpus import stopwords
from wordcloud import wordcloud, WordCloud



# 定义要处理的 CSV 文件路径
file_path = r"C:\Users\Boker\PycharmProjects\Emotion analysis\test1.csv"
data = pd.read_csv(open(file_path, encoding='gbk', errors='ignore')).astype(str)
# print(data.head())

stop_words = open(r'C:\Users\Boker\PycharmProjects\Emotion analysis\hit_stopwords.txt', 'r+', encoding='gb18030',
                  errors='ignore')
data_title_dep = data[["内容"]].copy().astype(str)  # 复制到新的地址，不破坏原始数据
data_title_dep1=data[["内容",data['情感倾向']=='1']].copy().astype(str)
newas = data_title_dep.loc[0:1000, "内容"]
newas1=data_title_dep.loc[ :,'内容':'情感倾向']
print(newas1)
# cut_df = cut_df[~cut_df.cut_words.isin(stopwords)]  # 用isin的反函数过滤词
# cut_word_list = cut_df['cut_words'].to_list()

# print(cut_word_list)
# # 定义要处理的列号
# column_number = 3

# 遍历数据列表，并去除停用词
# for row in data:
#     row_stripped = [word for word in row if word not in stop_words]
#     column_data = [row_stripped[3]]#有问题
#
#     # 将处理后的数据添加到新的数据列表中
#     data.append(column_data)
# print(data)
# # 将处理后的数据写入新的 CSV 文件
# with open(file_path, "w", encoding='gb18030') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow([""])
#     for row in data:
#         writer.writerow(row)


# def stopwordslist(filepath):  # 定义函数创建停用词列表
#     stopword = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  # 以行的形式读取停用词表，同时转换为列表
#     return stopword
#
#
# def delete_characters(token_words):
#     # 去除特殊字符、数字
#
#     words_list = re.sub('[\\u3000&a-zA-Z]', '', token_words)
#     end_list = re.sub('[0-9]', '', words_list)
#     # words_list = [word for word in token_words if word not in characters and not is_number(word)]
#     return end_list
#
# newdata = []
# lastsentences = []
# stopwords = stopwordslist("hit_stopwords.txt")
#
# def cutsentences(sentences):  # 定义函数实现分词
#     # print('原句子为：' + sentences)
#     newsentences = delete_characters(sentences)
#     # print('去除数字英文后：' +newsentences)
#     cutsentence = jieba.lcut(newsentences.strip())  # 精确模式
#     # print('\n' + '分词后：' + "/ ".join(cutsentence))
#     # 这里加载停用词的路径
#     for word in cutsentence:  # for循环遍历分词后的每个词语
#         if word not in stopwords:  # 判断分词后的词语是否在停用词表内
#             # if word != '\t':
#             # lastsentences += word
#             # lastsentences += "/ "
#             lastsentences.append(word)
#     return lastsentences
#     # print('\n' + '去除停用词后：' + lastsentences)
#
# a = []
# wordcount = []
# for i in newas:
#     a.append(cutsentences(i))
#     wordcount.extend(cutsentences(i))
#
# # 将Counter转换为DataFrame
# b = Counter(wordcount).most_common(20)
# # df = pd.DataFrame.from_dict(a, orient='index').reset_index()
# # print(df)
#
# print(a)
# # header = ['word', 'count']  # csv列名
# # with open('statistics.csv', 'w', encoding='utf-8',newline='') as f:
# #     writer = csv.writer(f)
# #     writer.writerow(header)
# #     for key, value in dict(b).items():# 转换为字典
# #         writer.writerow([key, value])
#


# df.to_csv('statistics.csv',encoding='utf-8')
# cutsentences("142yygd孤单的身影2562是德国，。。密码？?????第一")
# cutsentences("51654aaa打赏wekqm大事vx⑦")
#
# # for row in data_title_dep.iterrows():
# #     cutsentences(row)
# #     print(row)
# ds = pd.Series(wordCount).value_counts()#统计词频率
# print(newdata)
# print(ds)


# def remove_stopwords(text):
#     # 去除停用词
#     jieba_list = jieba.cut(text, cut_all=False)
#     return ''.join(jieba_list)
#
#
# print(remove_stopwords("142yygd孤单的身影2562是德国，。。密码？?????⑦第一"))
# str='''142yygd孤单的身影2562是德国，。。密码？?????⑦第一'''
# df = pd.read_csv(file_path, dtype=str, encoding='gb18030')
# # df = pd.get_dummies(df)
#
# df['内容'] = df['内容'].apply(remove_stopwords(stop_words))
#
# df.to_csv(file_path, encoding='gb18030', index=False)




#
# text_split_no_str = ' '.join(a)  # list类型分为str
# print(text_split_no_str)
# # 画词云
# mask = np.array(Image.open('22.jpg'))
# wordcloud = WordCloud(
#     # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
#     font_path="C:/Windows/Fonts/simfang.ttf", mask=mask, max_words=200,
#     # 设置了背景，宽高
#     background_color="white", width=800, height=1000).generate(text_split_no_str)  # text_split_no_str为字符串类型
#
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()