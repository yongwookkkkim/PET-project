import cv2
import numpy as np
from scipy.stats import gaussian_kde as kde

cap=cv2.VideoCapture(0)

#variables
lim=50
lbound=0.004

while True:
    success, frame=cap.read()
    #img=cv2.Canny(frame,250,300) 
    
    width=int(cap.get(3))
    height=int(cap.get(4))

    strip=frame[:,width//2]
    fr=strip[:,0]
    fg=strip[:,1]
    fb=strip[:,2]
    try:
        fr=kde(np.where(fr<lim)[0]).pdf(np.arange(height))
    except:
        fr=np.zeros(height)
    try:
        fg=kde(np.where(fg<lim)[0]).pdf(np.arange(height))
    except:
        fg=np.zeros(height)
    try:
        fb=kde(np.where(fb<lim)[0]).pdf(np.arange(height))
    except:
        fb=np.zeros(height)
    f=fr+fg+fb
    
    '''
    #basic functions
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
'''
    #vertical line
    img=cv2.line(frame, (width//2, 0), (width//2, height-1), (0,255,0), 2)

    #drawing line
    try:
        high=max(np.where(fr+fg+fb>lbound)[0])
        low=min(np.where(fr+fg+fb>lbound)[0])
        img=cv2.line(img, (0,high), (width-1,high), (0,0,255), 2)
        img=cv2.line(img, (0,low), (width-1,low), (0,0,255), 2)
    except:
        pass

    #display
    cv2.imshow("frame", img)
    
    #termination
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()