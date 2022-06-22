import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

dellim=50
recolim=50
tolerance=30

#open image and define width, height
#frame, 

frame1=cv2.resize(cv2.imread('kirkland2.jpg'), (480,640))
f1r=frame1[:,240,0]
try:
    f1r=sp.stats.gaussian_kde(np.where(f1r<50)).pdf(np.arange(640))
except:
    f1r=np.zeros(640)
f1g=frame1[:,240,1]
try:
    f1g=sp.stats.gaussian_kde(np.where(f1g<50)).pdf(np.arange(640))
except:
    f1g=np.zeros(640)
f1b=frame1[:,240,1]
try:
    f1b=sp.stats.gaussian_kde(np.where(f1b<50)).pdf(np.arange(640))
except:
    f1b=np.zeros(640)
'''
frame2=cv2.resize(cv2.imread('icis2.jpg'), (480,640))
frame3=cv2.resize(cv2.imread('icis3.jpg'), (480,640))
frame4=cv2.resize(cv2.imread('icis4.jpg'), (480,640))
frame5=cv2.resize(cv2.imread('kirkland1.jpg'), (480,640))
frame6=cv2.resize(cv2.imread('kirkland2.jpg'), (480,640))
frame7=cv2.resize(cv2.imread('kirkland3.jpg'), (480,640))
frame8=cv2.resize(cv2.imread('kirkland4.jpg'), (480,640))
'''
#plt.subplot(2,4,1)
plt.plot(np.arange(640),f1r+f1g+f1b)

#plt.title('icis1')
'''
plt.subplot(2,4,2)
plt.plot(np.arange(640),frame2[:,240])
plt.title('icis2')

plt.subplot(2,4,3)
plt.plot(np.arange(640),frame3[:,240])
plt.title('icis3')

plt.subplot(2,4,4)
plt.plot(np.arange(640),frame4[:,240])
plt.title('icis4')

plt.subplot(2,4,5)
plt.plot(np.arange(640),frame5[:,240])
plt.title('kirkland1')

plt.subplot(2,4,6)
plt.plot(np.arange(640),frame6[:,240])
plt.title('kirkland2')

plt.subplot(2,4,7)
plt.plot(np.arange(640),frame7[:,240])
plt.title('kirkland3')

plt.subplot(2,4,8)
plt.plot(np.arange(640),frame8[:,240])
plt.title('kirkland4')
'''
plt.show()
'''
height, width, channel=frame.shape

w0=np.arange(width)
h0=np.arange(height)
w,h=np.meshgrid(w0,h0)
frmg=lambda width, height: frame[height,width,0]-frame[height,width,1]
fgmb=lambda width, height: frame[height,width,1]-frame[height,width,2]
fbmr=lambda width, height: frame[height,width,2]-frame[height,width,0]
f0gmb=fgmb(w,h)
f0bmr=fbmr(w,h)
f0rmg=frmg(w,h)
    
    #digitalising
f0rmg=np.where(np.logical_and(f0rmg>-tolerance, f0rmg<tolerance),1,0)
f0bmr=np.where(np.logical_and(f0bmr>-tolerance, f0bmr<tolerance),1,0)
f0gmb=np.where(np.logical_and(f0gmb>-tolerance, f0gmb<tolerance),1,0)
ftot=f0gmb+f0bmr+f0rmg

#removing meaningless outliers / mutable
ftot[0:dellim,:]=3
ftot[height-dellim:height,:]=3

#recognising the limits
   

#print(np.where(ftot==0)[0])
print(ftot.shape)
strip=frame[:,width//2]
xax=np.arange(height)
plt.plot(xax,strip)
plt.show()

#vertical line
img=cv2.line(frame, (width//2, 0), (width//2, height-1), (0,255,0), 2)

#sp.stats.gaussian_kde

#drawing line
if len(np.where(ftot==0)[0])!=0:
    img=cv2.line(frame, (0,max(np.where(ftot==0)[0])), (width,max(np.where(ftot==0)[0])), (0,0,255), 2)
    img=cv2.line(frame, (0,min(np.where(ftot==0)[0])), (width,min(np.where(ftot==0)[0])), (0,0,255), 2)
else:
    img=frame


#display   
 
#while True:
#    cv2.imshow('frame',img) 
#    if cv2.waitKey(1)==ord('q'):
#        break
#cv2.destroyAllwindows() 
'''