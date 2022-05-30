from PIL import Image
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

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
    pix=img.load()
    width, height=img.size
    icis.append(im(pix,width,height))

for no in range(1,5):
    img=Image.open(f"kirkland{no}.jpg", 'r')
    pix=img.load()
    width, height=img.size
    kirkland.append(im(pix,width,height))


#plotting rgb difference graphs
x=range(kirkland[1].width)
y=range(kirkland[1].height)
x0,y0=np.meshgrid(x,y)
frmg=lambda a,b: kirkland[1].pix[a,b][0]-kirkland[1].pix[a,b][1]
fgmb=lambda a,b: kirkland[1].pix[a,b][1]-kirkland[1].pix[a,b][2]
fbmr=lambda a,b: kirkland[1].pix[a,b][2]-kirkland[1].pix[a,b][0]
f0rmg=[]
f0gmb=[]
f0bmr=[]
for height in y:
    rowrmg=[]
    rowgmb=[]
    rowbmr=[]
    for width in x:
        if fgmb(width,height)<30 and fgmb(width,height)>-30:
            rowgmb.append(100)
        else:
            rowgmb.append(0)

        if fbmr(width,height)<30 and fbmr(width,height)>-30:
            rowbmr.append(100)
        else:
            rowbmr.append(0)
        if frmg(width,height)<30 and frmg(width,height)>-30:
            rowrmg.append(100)
        else:
            rowrmg.append(0)
        #rowgmb.append(fgmb(width,height))
        #rowrmg.append(frmg(width,height))
        #rowbmr.append(fbmr(width,height))
    f0rmg.append(rowrmg)
    f0bmr.append(rowbmr)
    f0gmb.append(rowgmb)
plt.subplot(1,3,1)
plt.contour(x0,y0,f0rmg,[0])
plt.title("red minus green")

plt.subplot(1,3,2)
plt.contour(x0,y0,f0bmr,[0])
plt.title("blue minus red")

plt.subplot(1,3,3)
plt.contour(x0,y0,f0gmb,[0])
plt.title("green minus blue")

plt.tight_layout()
plt.show()