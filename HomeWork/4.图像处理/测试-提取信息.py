import matplotlib.pyplot as plt
import numpy as np

def plti(im, **kwargs):
    plt.imshow(im[:,:,], interpolation="none", **kwargs)
    #plt.axis('off') # 去掉坐标轴
    plt.show()

plt.subplots(1, 2, figsize=(6, 6))
img=plt.imread("G:\\尝试编程\python\homework\作业素材\星空.png")

b=np.array(img.shape)
b[0:2]=b[0:2]/2
im=np.zeros(tuple(b))
sum=np.zeros(tuple(b))

for t in range(0,720,2):                                #纵向循环
    for w in range(0,720,2):                            #横向循环
        for j in range (t,t+2):                         #四方格求和
            for i in range(w,w+2):
                sum=sum+img[i,j]/4

        im[w/2,t/2]=sum                               #将新生成的像素点赋到新的图里

plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plti(im)
# print(sum)