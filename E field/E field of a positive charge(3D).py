## E field of a positive charge in 3D

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-4,4,6)   #以6個向量標示
y = np.linspace(-4,4,6)
z = np.linspace(-4,4,6)
x,y,z = np.meshgrid(x,y,z)

# 3d figure
fig = plt.figure()
ax = fig.gca(projection='3d')  #畫出3維的座標軸

def E(x,y,z,m,n,l,q):     
    e=8.85*10**-12           
    EE = (1./(4*np.pi*e))*q/((x-m)**2+(y-n)**2+(z-l)**2) #Magnitude of the vector  電場
    Ex=EE*(x-m)/np.sqrt((x-m)**2+(y-n)**2+(z-l)**2)            #Ex: x方向電場 arctan2(y,x)是反tan(x/y)
    Ey=EE*(y-n)/np.sqrt((x-m)**2+(y-n)**2+(z-l)**2)         #Ey: y方向電場
    Ez=EE*(z-l)/np.sqrt((x-m)**2+(y-n)**2+(z-l)**2)         #Ez: z方向電場
    return Ex,Ey,Ez
Ex,Ey,Ez=E(x,y,z,0,0,0,2)
ax.quiver(x,y,z,Ex,Ey,Ez,color='b',length=1,normalize=True) 
plt.title('E field of a positive charge')
plt.xlabel('x')
plt.ylabel('y')
plt.ylabel('z')
plt.plot
#ax.view_init(elev=-90, azim=90)
#for angle in range(0, 360):
    #ax.view_init(30,angle)
plt.plot( [0], [0], [0], color='red', marker='o', markersize=12)   #畫出電荷位置


plt.show()