import cv2
import numpy as np
from scipy.stats import gaussian_kde as kde

cap=cv2.VideoCapture(0)

#variables
lim=50
lbound=0.004

while True:
    success, frame=cap.read()
    
    width=int(cap.get(3))
    height=int(cap.get(4))

    #distribution
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