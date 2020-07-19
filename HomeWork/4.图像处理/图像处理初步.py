import numpy as np
import matplotlib.pylab as plt

#显示图像函数
def plti(im, **kwargs):
    plt.imshow(im[:,:,], interpolation="none", **kwargs)
    #plt.axis('off') # 去掉坐标轴
    plt.show()

#缩小操作
def reduce(img):
    plt.subplots(1,2,figsize=(6,6))
    i=int(input('请输入需要缩小的倍数n：\n'))
    print("缩小的倍数n=",i)

    plt.subplot(1,2,1)
    im = img[::i, ::i, :]
    plt.imshow(img)
    plt.subplot(1,2,2)
    plti(im)

#将图片放大2倍
def enlarge(img):
    plt.subplots(1, 2, figsize=(6, 6))
    num=np.array(img.shape)                                         #将原图像的大小信息提取出来以便进行缩放操作
    num[0:2]=num[0:2]*2
    im_new=np.zeros(tuple(num))                                     #初始化新图像

    im_new[:-1:2,:-1:2,:]=img[::,::,:]                              #将原图像中的信息隔行隔列插入新图中
    im_new[::2,1:-1:2,:]=(img[::,:-1:,:]+img[::,1::,:])/2           #行信息取平均
    im_new[1:-1:2,::2,:]=(img[:-1:,::,:]+img[1::,::,:])/2           #列信息平均
    im_new[1:-1:2,1:-1:2,:]=(img[:-1:,:-1:,:]+img[1::,1::,:])/2     #对角线信息区平均

    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.subplot(1,2,2)
    plti(im_new)

img=plt.imread("H:/尝试编程/python\homework/作业素材/lena512color.png")
reduce(img)
enlarge(img)