import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from skimage import data,img_as_float

## 读##取AIA fits
## hdu = fits.open('H:/尝试编程/python/homework/作业素材/fit500sdss/spSpec-51612-0280-152.fit')
##  #hdu.info();
##hdu.verify('fix')
## #hdu[1].data;
##img_data_aia = np.flipud(hdu[1].data)

### 读取EIT fits

hdu = fits.open('H:/尝试编程/python/homework/作业素材/fit500sdss/spSpec-51612-0280-152.fit')
#hdu.info()
# img_data = hdu[1].data

# img_name="H:/尝试编程/python/homework/作业素材/fit500sdss/spSpec-51612-0280-152.fit"
# dst=img_as_float(hdu)

Y = np.float32(hdu[1])

# print(type(dst))
# print(type(hdu))

# print(hdu[1].columns)

## 显示fits图像
# plt.imshow(dst, cmap= 'gray')
# plt.colorbar()
# plt.show()