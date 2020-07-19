import numpy as np
import matplotlib.pyplot as plt

im0=plt.imread("G:\\尝试编程\python\homework\作业素材\lena512color.tiff")
k=2
num = np.array(im0.shape)                # 将原图像的大小信息提取出来以便进行缩放操作
num[0:2] = num[0:2] * k
im_n = np.zeros(tuple(num))              # 生成新图像
im_n[::k,::k,:]= im0[::, ::, :]          #将原图像中的信息隔行隔列插入新图中

def Lr(i,k,im,c):
    #三次拉格朗日插值
    s = 0
    for n in range(1,k):                   # 插入 n = k-1 个值 , k为放大倍数
        for g in range(4):                 # 累加
            w = 1
            for h in range(4):             # 累乘
                if(h!=g):
                    w=w*((n-1)*(n-2)*(n-3)/(-6*k**3))
            s = s + w * im[ : , : ]         # 计算插值
        im_n[i : i+4 ,::k, c]=s              # 将插值放入新的图像
def fcr(img,k):
    #  计算方差,横向放大
    for i in range(2,509):
        for c in range(3):
            # 原图像分割，取出纵向数据
            p1R = img[  i  : i + 4, :, c]
            p2R = img[i + 1: i + 5, :, c]
            p3R = img[i + 2: i + 6, :, c]

            # 平均值
            p1 = p1R[0, :] / 400 + p1R[1, :] / 400 + p1R[2, :] / 400 + p1R[3, :] / 400
            p2 = p2R[0, :] / 400 + p2R[1, :] / 400 + p2R[2, :] / 400 + p2R[3, :] / 400
            p3 = p3R[0, :] / 400 + p3R[1, :] / 400 + p3R[2, :] / 400 + p3R[3, :] / 400
            # 方差
            S1 = (p1R[0] / 100) ** 2 + (p1R[1] / 100) ** 2 - 0.4 * p1 ** 2
            S2 = (p2R[0] / 100) ** 2 + (p2R[3] / 100) ** 2 - 0.4 * p2 ** 2
            S3 = (p3R[2] / 100) ** 2 + (p3R[3] / 100) ** 2 - 0.4 * p3 ** 2

            # 筛选合适的数据进行插值计算
            S=[S1[i],S2[i],S3[i]]
            m=max(S)
            if (m == S1[i]):
                Lr(i,k,p1R,c)
            if (m == S2[i]):
                Lr(i,k,p2R,c)
            if (m == S3[i]):
                Lr(i,k,p3R,c)

def Lv(i,k,im,c):
    #三次拉格朗日插值
    s = 0
    for n in range(1,k):                   # 插入 n = k-1 个值 , k为放大倍数
        for g in range(4):                 # 累加
            w = 1
            for h in range(4):             # 累乘
                if(h!=g):
                    w=w*((n-1)*(n-2)*(n-3)/(-6*k**3))
            s = s + w * im[ : , : ]         # 计算插值
        im_n[i : i+4 ,::, c]=s              # 将插值放入新的图像
def fcv(img,k):
    #  计算方差,横向放大
    for i in range(2,509):
        for c in range(3):
            # 原图像分割，取出纵向数据
            p1R = img[  i  : i + 4, :, c]
            p2R = img[i + 1: i + 5, :, c]
            p3R = img[i + 2: i + 6, :, c]

            # 平均值
            p1 = p1R[0, :] / 400 + p1R[1, :] / 400 + p1R[2, :] / 400 + p1R[3, :] / 400
            p2 = p2R[0, :] / 400 + p2R[1, :] / 400 + p2R[2, :] / 400 + p2R[3, :] / 400
            p3 = p3R[0, :] / 400 + p3R[1, :] / 400 + p3R[2, :] / 400 + p3R[3, :] / 400
            # 方差
            S1 = (p1R[0] / 100) ** 2 + (p1R[1] / 100) ** 2 - 0.4 * p1 ** 2
            S2 = (p2R[0] / 100) ** 2 + (p2R[3] / 100) ** 2 - 0.4 * p2 ** 2
            S3 = (p3R[2] / 100) ** 2 + (p3R[3] / 100) ** 2 - 0.4 * p3 ** 2

            # 筛选合适的数据进行插值计算
            S=[S1[i],S2[i],S3[i]]
            m=max(S)
            if (m == S1[i]):
                Lv(i,k,p1R,c)
            if (m == S2[i]):
                Lv(i,k,p2R,c)
            if (m == S3[i]):
                Lv(i,k,p3R,c)

fcr(im0,2)
ims = np.zeros_like(im_n)                   # 将图像逆时针旋转90度，继续进行处理
ims[:,:,0]=im_n[:,:,0].T                    # 单通道转置操作
ims[:,:,1]=im_n[:,:,1].T
ims[:,:,2]=im_n[:,:,2].T
fcv(ims,2)

plt.imshow(im_n)
plt.show()

# o=im_n[0 : 4 ,::2 ]
# t=ims[ 2:  6, :]
# print(im_n.shape)
# print(t.shape)
# print(o.shape)