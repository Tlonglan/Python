import numpy as np
import matplotlib.pyplot as plt

# img = plt.imread("G:\\尝试编程\python\homework\作业素材\lena512color.tiff")
x=np.array([5,10,2,8,6,11]);y=x**3+10
print(type(x))
# def max(x):
#     #最大值函数
#     a=np.max(x)
#     print(a)

def lagrange(q):
    #三次拉格朗日插值
    # print('需要插值的q的位置:')
    k=len(x)
    s=0
    for i in range(k):                  #累加
        w = 1
        for j in range(k):              #累乘
            if(j!=i):
                w=w*(q-x[j])/(x[i]-x[j])
        s = s + w*y[i]
    print('q=',q,'\n','s=',s)
q=float(input('想知道q对应的值:'));lagrange(q)

# def large(img):
#     # 初始化放大图像
#     # plt.subplots(1, 2, figsize=(6, 6))
#     num = np.array(img.shape)  # 将原图像的大小信息提取出来以便进行缩放操作
#     num[0:2] = num[0:2] * 2
#     new = np.zeros(tuple(num))  # 初始化新图像

# # t=(img[0,0:4]**2)/2+(img[66,1:5]**2)/2
# # p1=img[0:4,:,:]
# # p2=img[1:5,:,:]
# # q=float(input())
# # lagrange(q)
# yb=6*x
# print(x*yb)


# import numpy as np
# import matplotlib.pylab as plt
# img=plt.imread("G:\\尝试编程\python\homework\作业素材\lena512color.png")
#
# #显示图像函数
# def plti(im, **kwargs):
#     plt.imshow(im[:,:,], interpolation="none", **kwargs)
#     #plt.axis('off') # 去掉坐标轴
#     plt.show()
# def enlarge(img):
#     num=np.array(img.shape)                                         #将原图像的大小信息提取出来以便进行缩放操作
#     num[0:2]=num[0:2]*2
#     im_new=np.zeros(tuple(num))                                     #初始化新图像
#
#     im_new[:-1:2,:-1:2,:]=img[::,::,:]                              #将原图像中的信息隔行隔列插入新图中
#     plti(im_new)
#     k = 2
#     num = np.array(img.shape)  # 将原图像的大小信息提取出来以便进行缩放操作
#     num[0:2] = num[0:2] * k
#     im_n = np.zeros(tuple(num))  # 生成新图像
#     im_n[::k, ::k, :] = img[::, ::, :]  # 将原图像中的信息隔行隔列插入新图中
#
#     def L(i, k, im, c):
#         # 三次拉格朗日插值
#         s = 0
#         for n in range(1, k):  # 插入 n = k-1 个值 , k为放大倍数
#             for g in range(4):  # 累加
#                 w = 1
#                 for h in range(4):  # 累乘
#                     if (h != g):
#                         w = w * ((n - 1) * (n - 2) * (n - 3) / (-6 * k ** 3))
#                 s = s + w * im[:, :]  # 计算插值
#             im_n[i: i + 4, ::k, c] = s  # 将插值放入新的图像
#             return im_n
#
#     def fc(img, k):
#         #  计算方差,横向放大
#         for i in range(3, 410):
#             for c in range(3):
#                 d = [(1024, 1024, 3)]
#                 # 原图像分割
#                 p1R = img[  i  : i + 4, :, c]
#                 p2R = img[i + 1: i + 5, :, c]
#                 p3R = img[i + 2: i + 6, :, c]
#
#                 # 平均值
#                 p1 = p1R[0, :] / 400 + p1R[1, :] / 400 + p1R[2, :] / 400 + p1R[3, :] / 400
#                 p2 = p2R[0, :] / 400 + p2R[1, :] / 400 + p2R[2, :] / 400 + p2R[3, :] / 400
#                 p3 = p3R[0, :] / 400 + p3R[1, :] / 400 + p3R[2, :] / 400 + p3R[3, :] / 400
#                 # 方差
#                 S1 = (p1R[0] / 100) ** 2 + (p1R[1] / 100) ** 2 - 0.4 * p1 ** 2
#                 S2 = (p2R[0] / 100) ** 2 + (p2R[3] / 100) ** 2 - 0.4 * p2 ** 2
#                 S3 = (p3R[2] / 100) ** 2 + (p3R[3] / 100) ** 2 - 0.4 * p3 ** 2
#
#                 # 筛选合适的数据进行插值计算
#                 m = max(S1[i], S2[i], S3[i])
#                 if (m == S1[i]):
#                     L(i, k, p1R, c)
#                 if (m == S2[i]):
#                     L(i, k, p2R, c)
#                 if (m == S3[i]):
#                     L(i, k, p3R, c)
#
#  # def Lv(i,k,im,c):
#     #     #三次拉格朗日插值
#     #     s = 0
#     #     for n in range(1,k):                   # 插入 n = k-1 个值 , k为放大倍数
#     #         for g in range(4):                 # 累加
#     #             w = 1
#     #             for h in range(4):             # 累乘
#     #                 if(h!=g):
#     #                     w=w*((n-1)*(n-2)*(n-3)/(-6*k**3))
#     #             s = s + w * im[ : , : ]            # 计算插值
#     #         im_n[::k, i : i+4 , c]=s             # 将插值放入新的图像
#     #         return im_n
#     # def fcv(img,k):
#     #     #  计算方差,纵向放大
#     #     for i in range(3,410):
#     #         for c in range(3):
#     #             # 原图像分割
#     #             p1R = img[  :,   i  : i + 4,  c]
#     #             p2R = img[  :, i + 1: i + 5,  c]
#     #             p3R = img[  :, i + 2: i + 6,  c]
#     #
#     #             # 平均值
#     #             p_1 = p1R[:, 0] / 400 + p1R[:, 1] / 400 + p1R[:, 2] / 400 + p1R[:, 3] / 400
#     #             p_2 = p2R[:, 0] / 400 + p2R[:, 1] / 400 + p2R[:, 2] / 400 + p2R[:, 3] / 400
#     #             p_3 = p3R[:, 0] / 400 + p3R[:, 1] / 400 + p3R[:, 2] / 400 + p3R[:, 3] / 400
#     #             w1 = np.array(p_1)
#     #             p1 = w1.reshape(512, 1)
#     #             w2 = np.array(p_2)
#     #             p2 = w2.reshape(512, 1)
#     #             w3 = np.array(p_3)
#     #             p3 = w3.reshape(512, 1)
#     #             # 方差
#     #             S1 = (p1R[0] / 100) ** 2 + (p1R[1] / 100) ** 2 - 0.4 * p1 ** 2
#     #             S2 = (p2R[0] / 100) ** 2 + (p2R[3] / 100) ** 2 - 0.4 * p2 ** 2
#     #             S3 = (p3R[2] / 100) ** 2 + (p3R[3] / 100) ** 2 - 0.4 * p3 ** 2
#     #
#     #             # 筛选合适的数据进行插值计算
#     #             # for v in range(4):
#     #             S = [S1[i][0], S2[i][0], S3[i][0]]
#     #             m = max(S)
#     #             if (m == S1[i]):
#     #                 Lv(i, k, p1R, c)
#     #             if (m == S2[i]):
#     #                 Lv(i, k, p2R, c)
#     #             if (m == S3[i]):
#     #                 Lv(i, k, p3R, c)
#
#     fc(img, 2)
#     # fcv(im0,2)
#     plt.imshow(im_n)
#     plt.show()
# enlarge(img)