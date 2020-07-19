import numpy as np
import matplotlib.pyplot as plt

def squarloop():
	a=np.arange(1,5)
	b=a.reshape(2,2)
	print(b)
	w=0

	for j in range(0,2):
		for i in range(0,2):
			w=w+b[i,j]

	print(w)

def info():
	img=plt.imread("G:\\尝试编程\python\homework\作业素材\星空.png")
	w=img[0,1]
	print(w)

def imginfo():
	img=plt.imread("G:\\尝试编程\python\homework\作业素材\星空.png")
	b=np.array(img.shape)
	b[0:2]=b[0:2]/2
	im_i = img[::2,::2]
	im_j = img[::2, 1::2]
	im_k = img[1::2, ::2]
	im_m = img[1::2, 1::2]

	im_new=(im_i+im_j+im_k+im_m)/4
	plt.imshow(im_new)
	plt.show()
#squarloop()
imginfo()