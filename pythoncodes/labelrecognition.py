import cv2
import numpy as np

cap=cv2.VideoCapture(1)

#variables
dellim=50
recolim=50
tolerance=76

while True:
    success, frame=cap.read()
    img=cv2.Canny(frame,250,300)
    '''
    width=int(cap.get(3))
    height=int(cap.get(4))

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

    #drawing line
    if len(np.where(ftot==0)[0])!=0:
        img=cv2.line(frame, (0,max(np.where(ftot==0)[0])), (width,max(np.where(ftot==0)[0])), (0,0,255), 2)
        img=cv2.line(frame, (0,min(np.where(ftot==0)[0])), (width,min(np.where(ftot==0)[0])), (0,0,255), 2)
    else:
        img=frame
    '''
    #display
    cv2.imshow("frame", img)
    
    #termination
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()