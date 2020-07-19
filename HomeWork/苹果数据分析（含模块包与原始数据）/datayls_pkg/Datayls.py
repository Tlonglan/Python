import numpy as np
from pandas import Series,DataFrame
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
#给绘图模块添加中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']

#某段时间内的交易平均价格
def Ave(data):
    global ave
    a=Series(data[:,1])
    b=Series(data[:,2])
    s_h=Series(np.array(a.sort_values()))               #最高价从小到大重新排序
    s_l=Series(np.array(b.sort_values()))               #最低价从小到大重新排序
    ave=(s_h[442]+ s_l[0])/2                            #此段时间的平均价
    print('该时间段平均价格为：',ave)

#某段时间内的交易价格走向图
def Pl(data):
    x = np.array(range(443))
    yo = data[:, 0]
    yc = data[:, 3]
    nave = zeros_like(x)
    nave[:] = ave
    plt.figure(figsize=(10, 5))
    plt.plot(x, yo, color='red', linestyle='-.', linewidth=0.75, label=u'最高价走势')
    plt.plot(x, yc, 'b--', linewidth=0.75, label=u'最低价走势')
    plt.xlabel(u'日期')
    plt.ylabel(u'价格')
    plt.plot(x, nave, 'k-', label=u'此段时间内平均价格')
    plt.legend()
    plt.title(u'2015苹果公司股票部分数据')
    plt.show()

#某段时间内每天的价格与平均价格的比较结果
def Ndat(data):
    avd = (data[:, 1] + data[:, 2]) / 2
    favd = DataFrame(avd)                               # 将每天的平均价转成DataFrame形式
    u = favd[favd[:].values < ave]                      # 将符合条件的值筛选出来
    d = favd[favd[:].values > ave]
    up = u.values                                       # 除去缺省值，将有效值提取到新的Dataframe中，
    down = d.values
    nup = up.reshape(-1, 1)                             # 将只装着符合条件的值的新的DataFrame转成数组
    ndown = down.reshape(-1, 1)
    print('当天价格高于该时间段平均价格的天数为：', len(nup),'天')
    print('当天价格低于该时间段平均价格的天数为：', len(ndown),'天')