# coding=utf-8
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, colors
from pandas._libs.reshape import explode
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie
from pyecharts.faker import Faker
from wordcloud import wordcloud

plt.rcParams['font.sans-serif'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False

filepath = "statistics.csv"
filepath1 = "emo.csv"
data = pd.read_csv(filepath, names=["词语", "词频数"], usecols=[0, 1])
data1 = pd.read_csv(filepath1)

data1= np.array(data1)

# print(data1)
# 使pyechart中的bar对点赞top50进行柱状图可视化呈现，滚动加载
#
#
# 用pyechart呈现出可以拖动的条形图，灵活呈现该视频的点赞情况
# bar = (
#     Bar()
#     .add_xaxis(data["词语"].to_list())
#     .add_yaxis("词频数", data["词频数"].to_list(), color=Faker.rand_color())
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="词频Top20"),
#         datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
#     )
#     .render("词频排序.html")
# )
d=data1[0][1]+data1[1][1]+data1[2][1]
a1=f"{round(float(data1[0][1]/d) * 100,2)}%"
a2=f"{round(float(data1[1][1]/d) * 100,2)}%"
a3=f"{round(float(data1[2][1]/d) * 100,2)}%"
# print(a1,a2,a3)
# 显示出百分比
plt.pie(data1[:, 1], labels=['消极'+a1, '中性'+a2, '积极'+ a3])  # 数据为文件的第1列（从第0列开始）
plt.legend(['消极', '中性', '积极'], loc="upper left")
plt.title('情感倾向')
# 显示图表
plt.show()
