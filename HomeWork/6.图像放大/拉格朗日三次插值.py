import numpy as np
import matplotlib.pyplot as plt

# img=plt.imread("G:\\尝试编程\python\homework\作业素材\lena512color.tiff")
# # plt.subplots(1, 2, figsize=(6, 6))
# num = np.array(img.shape)  # 将原图像的大小信息提取出来以便进行缩放操作
# num[0:2] = num[0:2] * 2
# im = np.zeros(tuple(num))  # 初始化新图像
#
# im[:-1:2, :-1:2, :] = img[::, ::, :]  # 将原图像中的信息隔行隔列插入新图中
# plt.imshow(img)
# plt.show()
p=[0,1,2,3]
t=np.array(p)
w=t.reshape(2,2)
print(w[1][1])