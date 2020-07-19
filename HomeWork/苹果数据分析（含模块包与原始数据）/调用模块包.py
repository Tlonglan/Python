from datayls_pkg import Datayls
import numpy as np

data=np.loadtxt("G:\\尝试编程\python\homework\作业素材\苹果数据.csv",skiprows=1,delimiter=',',usecols=(1,2,3,4,5))          #载入价格数据

Datayls.Ave(data)
Datayls.Pl(data)
Datayls.Ndat(data)