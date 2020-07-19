from pandas import Series,DataFrame
import pandas as pd
import numpy as np

# a=Series([-5,5,-1,3])
# b=a.sort_values()
# c=Series(np.array(b))
# print(a)
# print(b)
# print(c)
# print(c[3])
# a=np.array(1)
# # a=np.arange(10)
# # print(a)
# b=a.reshape()
# print(b)

a=np.array(range(20))
b=a.reshape(10,2)
c=b.tolist()
print(b)