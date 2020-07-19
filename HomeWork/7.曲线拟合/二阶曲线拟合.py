import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']
mpl.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(9,9))

x = np.linspace(-5,5,1000)
X = np.array([0., 1., 2., 3., -1., -2., -3.])
Y = np.array([-1.22, 1.85, 3.22, 10.29, 2.21, 3.72, 8.7])

def f(p):
    a, b, c = p
    return(Y-(a*X**2+b*X+c))

x0 = np.array([1,1,1])              # 拟合的初始参数

r = leastsq(f, x0)
a, b, c = r[0]
print("a=",a,"b=",b, "c=",c)

plt.scatter(X,Y, s=100, alpha=1.0, marker='o',label=u'数据点')

y=a*x**2+b*x+c

ax = plt.gca()

ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)
# 设置坐标轴标签字体大小

plt.plot(x, y, color='r',linewidth=5, linestyle=":",markersize=20, label=u'拟合曲线')

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')

plt.xlabel(u'电流/A')
plt.ylabel(u'热量/J')

plt.xlim(x.min(), x.max() * 1.1)
plt.ylim(y.min(), y.max() * 1.1)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#刻度字体大小
plt.legend(loc='upper left')
plt.show()