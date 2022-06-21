from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from matplotlib import cm

icis=[]
kirkland=[]
class im():
    def __init__(self, pix, width, height):
        self.pix=pix
        self.width=width
        self.height=height

#loading images
for no in range(1,5):
    img=Image.open(f"icis{no}.jpg", 'r')
    width, height=img.size
    pix=np.array(img,dtype='int16')
    icis.append(im(pix,width,height))

for no in range(1,5):
    img=Image.open(f"kirkland{no}.jpg", 'r')
    width, height=img.size
    pix=np.array(img,dtype='int16')
    kirkland.append(im(pix,width,height))

#processing data for rgb difference graphs
w0=np.arange(icis[2].width,dtype='int16')
h0=np.arange(icis[2].height,dtype='int16')
w,h=np.meshgrid(w0,h0)
frmg=lambda width, height: icis[2].pix[height,width,0]-icis[2].pix[height,width,1]
fgmb=lambda width, height: icis[2].pix[height,width,1]-icis[2].pix[height,width,2]
fbmr=lambda width, height: icis[2].pix[height,width,2]-icis[2].pix[height,width,0]
f0gmb=fgmb(w,h)
f0bmr=fbmr(w,h)
f0rmg=frmg(w,h)
f0rmg=np.where(np.logical_and(f0rmg>-30, f0rmg<30),1,0)
f0bmr=np.where(np.logical_and(f0bmr>-30, f0bmr<30),1,0)
f0gmb=np.where(np.logical_and(f0gmb>-30, f0gmb<30),1,0)
#f0rmg[np.logical_and(f0rmg>-30, f0rmg<30)]=100
#f0rmg[f0rmg!=100]=0

#removing meaningless outliers / mutable
#bottom
'''
f0bmr[0:280,:]=1
f0gmb[0:280,:]=1
f0rmg[0:280,:]=1
#top
f0bmr[1350:,:]=1
f0gmb[1350:,:]=1
f0rmg[1350:,:]=1
#left
f0bmr[:,0:200]=1
f0gmb[:,0:200]=1
f0rmg[:,0:200]=1
#right
f0bmr[:,1000:]=1
f0gmb[:,1000:]=1
f0rmg[:,1000:]=1


print(f0rmg[1:100,0])
print(np.where(f0bmr==1)[0])

#distribution
print(gaussian_kde(f0bmr[:,0]))
'''

ftot=f0gmb+f0bmr+f0rmg
print(max(np.where(ftot==0)[0]))
print(min(np.where(ftot==0)[0]))

#plotting
fig = plt.figure(figsize = [12, 8])
ax = fig.gca(projection = '3d') #set up the axis as a 3d plot
ax.plot_surface(w,h,ftot,cmap=cm.coolwarm) 
#coolwarm, copper, cubehellix, Dark2, flag, dated, copper

plt.show()

'''
plt.subplot(1,3,1)
plt.contour(w,h,f0rmg,[0])
plt.title("red minus green")

plt.subplot(1,3,2)
plt.contour(w,h,f0bmr,[0])
plt.title("blue minus red")

plt.subplot(1,3,3)
plt.contour(w,h,f0gmb+f0bmr+f0rmg,[0])
plt.title("green minus blue")

plt.tight_layout()
plt.show()
'''