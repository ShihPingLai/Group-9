import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2.5,2.5,20)
y = np.linspace(-2.5,2.5,20)
x,y = np.meshgrid(x,y)

# 2d figure
fig = plt.figure()
ax = fig.add_subplot(111)  #畫出2維的座標軸

def E(x,y,m,n,q):     
    e=8.85*10**-12           
    EE = (1./(4*np.pi*e))*q/((x-m)**2+(y-n)**2) #Magnitude of the vector E 磁場
    Ex=EE*(np.cos(np.arctan2(y-n,x-m)))            #Ey y方向磁場 arctan2(y,x)是反tan(x/y)
    Ey=EE*(np.sin(np.arctan2(y-n,x-m)))           #Ex x方向磁場
 
    return Ex,Ey

Ex, Ey = E(x,y,0,0,2)

plt.quiver(x,y,Ex,Ey,width=0.03,units='xy',color='b', scale = 30000000000) 

plt.title('E field of a positive charge in 2D')
plt.xlabel('x')
plt.ylabel('y')
#ax.view_init(elev=-90, azim=90)
#for angle in range(0, 360):
    #ax.view_init(30, angle)
    
plt.plot( [0], [0], color='red', marker='o', markersize=10)
    
plt.show()
