import numpy as np
import matplotlib.pylab as plt

def plti(im, **kwargs):
    plt.imshow(im, interpolation="none", **kwargs)
    plt.axis('off') # 去掉坐标轴
    plt.show() # 弹窗显示图像

# 加载图像
im = plt.imread("G:\\尝试编程\python\homework\作业素材\lena512color.png") # 加载当前文件夹中名为BTD.jpg的图片
# im = im[::8,::8,:]
# print(im.shape) # 输出图像尺寸
# plti(im)

# # im = im[400:3800,:2000,:]  # 直接切片对图像进行裁剪
# # plti(im)
#
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15,5))
# # 将一张图分为1x3个子图，axs为各子图对象构成的列表。figsize为显示窗口的横纵比。
#
for c, ax in zip(range(3), axs): # 使用zip来同时循环3通道和3个子图对象——zip()函数将相同维度上的元素打包组成该维度上的新元素
    tmp_im = np.zeros(im.shape) # 初始化一个和原图像大小相同的三维数组
    # 注意 tmp_im 仍然是三通道
    tmp_im[:,:,c] = im[:,:,c] # 只复制某一通道
    one_channel = im[:,:,c].flatten() # 索引该通道并展平至一维
    print("channel", c, " max = ", max(one_channel), "min = ", min(one_channel)) # 输出该通道最大最小的像素值
    ax.imshow(tmp_im) # 在子图上绘制
    ax.set_axis_off() # 去掉子图坐标轴
# 注意以上 tmp_im 采用的是切片复制
plt.show()