from matplotlib import pyplot
import numpy as np


def get_var_list(img, color):
    m, n, c = img.shape
    var_array = np.zeros((m, n)) #创建一个与原图shape一样的二维数组
    for j in range(n): #先遍历列 可以让边缘判断更加简易
        if j + 3 > n - 1: #边缘判断 右边 因为每个点都是计算向右4个点的方差 所以右边最后3个点是没有方差可以算的
            var_array[::, j] = var_array[::, j - 1]
            continue
        for i in range(m):
            dot_list = []
            for l in range(4):#先将4个点放入一个数组里
                dot_list.append(img[i, j + l, color])
            var_array[i, j] = np.var(dot_list) #在将四个点的方差计算出来放入方差数组
    print('var done')
    return var_array


def lagrange(img, x, y, c, y0): # 三次拉格朗日插值
    t = 0.0
    for i in range(4):
        u = 1.0
        for j in range(4):
            if i != j:
                u *= (y - y0 - j) / (i - j)
        t += u * img[x, y0 + i, c]
    return t


def interp(img, k):
    m, n, c = img.shape
    img_work = np.zeros((m, k, c))
    for color in range(c): #先遍历颜色 用以计算方差数组
        var_array = get_var_list(img, color) #计算当前颜色所有点的方差值
        for i in range(m):
            for j in range(k):
                x = i
                y = j * n / k #计算出映射到原图的目标点列坐标
                y_int = np.int(y) 
                if y_int - 2 < 0: #边缘判断 左边
                    y0 = 0
                elif y_int + 4 > n - 1: #边缘判断 右边
                    y0 = n - 5
                else:
                    y0 = y_int - 2 + np.argmin(var_array[x, y_int - 2:y_int + 1]) #y0就是6个点分成3组后 方差最小的那组的第一个点的坐标
                img_work[i, j, color] = lagrange(img, x, y, color, y0) #拉格朗日函数 原图 目标点的映射坐标(x,y) 颜色color 与y0作为参数
                if (i + 1) % 128 == 0 and j == 0:
                    print(i + 1, j)
    return img_work


img = pyplot.imread('lena512color.tiff')
k, l = 768, 768
# 先做横向插值
img_1 = np.transpose(interp(img, k), axes=(1, 0, 2)) #得出结果后转置
# 再做竖向插值
img_2 = np.transpose(interp(img_1, l), axes=(1, 0, 2)) #将转置切插值后的图片再转置回来
pyplot.imshow(np.uint8(img_2))
pyplot.show()
pyplot.imsave('lena512color`.tiff', np.uint8(img_2))
