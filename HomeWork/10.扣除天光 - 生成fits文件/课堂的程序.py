import numpy as np
import matplotlib.pylab as plt
from astropy.io import fits

hdu= fits.open('H:/尝试编程/python/homework/作业素材/spSpec-51612-0280-152.fit')

lgλ0= np.array( hdu[0].header['coeff0'] )
lgΔλ= np.array( hdu[0].header['coeff1'] )
N=np.array( hdu[0].header['naxis1'] )
λn=np.array( [i for i in range(N)] )

wave=10**(lgλ0+lgΔλ*λn)
flux= hdu[0].data[0]
err= hdu[0].data[2]

plt.plot(wave,flux)
plt.plot(wave,err)

NBINS = 1000
# histogram = plt.hist(hdu.flatten(), NBINS)
plt.show()

print(np.float32(wave)[0:10])