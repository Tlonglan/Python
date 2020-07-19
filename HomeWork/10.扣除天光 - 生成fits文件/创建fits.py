import numpy as np
from astropy.io import fits
import matplotlib.pylab as plt

# hdu = fits.open('H:/尝试编程/python/homework/作业素材/fit500sdss/spSpec-51612-0280-152.fit')
# hdu.info()

im0 = plt.imread('G:/0回忆/正装.jpg')
im = im0[:,:,0]
hdu = fits.PrimaryHDU(im)
hdu.header['name'] = "Jiaming Jian"
hdu.header['ID'] = ('1519100045','student ID of me in the school')
hdu.header['sex'] = 'man'
hdu.header['age'] = ('3','age of the me')
hdu.header['height'] = ('169',' the unit is cm')
hdu.header['weight'] = ('56','the unit is kg')
hdu.header['eyesight'] = '5.2'
hdu.header['phone'] = '13266666666'
hdu.header['mail'] = '510000000@qq.com'

hdu.header['Uni'] = ('Guangzhou University','my university')
hdu.header['class'] = 'physics class 2'
hdu.header.set('school', 'Physics and Electronics engineering School', before = 'Uni')
hdu.header['EduBg'] = ('undergrate', 'Education background')
# hdu.header['UnOrg'] = ('Information Center of Work - Study ','the organization of univercity that I had joined ')
# hdu.header['ScAss'] = ('Association of Young Volunteers ','the association of school that I had joined ')

hdu.header.set('skill', 'NCER-2, CET-4, PSC-2A', 'PSC is PUTONGHUA SHUIPING CESHI')
hdu.header.set('honor','Awarded third scholarship in the school')

hdu.header.set('cha','active','my evaluation')
hdu.header.set('hobby','Making Videos,Taichi')
hdu.header.set('spe','ping-pong','the thing I am shilled in')

hdu.header.append(('Book','the Best of Us','my favourite book'),end = True)
hdu.header.append(('song', 'If We Never Met', 'my favourite song and it was song by LunSang '),end = True)
hdu.header.append(('char','POWPOWBING', 'my favourite charcater'),end = True)
hdu.header.append(('food','Rice with Mushroom and Meet slices', 'my favourite food'),end = True)
hdu.header.append(('Hth','Direct others','the thing I hate to do'),end = True)

hdu.header.set('goal','become an excellent dynamic visual designer','the job I want to join',after = 'Hth')
hdu.header.set('state','preparing the final test','my recent state ')

hdu.writeto('CV-O-JJM.fits')
