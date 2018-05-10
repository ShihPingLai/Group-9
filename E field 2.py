from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-4,4,10)
y = np.linspace(-4,4,10)
z = np.linspace(-4,4,10)
x,y,z = np.meshgrid(x,y,z)
# 3d figure
fig = plt.figure()
ax = fig.gca(projection='3d')  #畫出3維的座標軸

def E(x,y,m,n,q):     
    e=8.85*10**-12           
    EE = (1./(4*np.pi*e))*q/((x-m)**2+(y-n)**2) #Magnitude of the vector B 磁場
    Ex=EE*(np.cos(np.arctan2(y-n,x-m)))            #By y方向磁場 arctan2(y,x)是反tan(x/y)
    Ey=EE*(np.sin(np.arctan2(y-n,x-m)))           #Bx x方向磁場
    Ez=0
    return Ex,Ey,Ez
Ex,Ey,Ez=E(x,y,0,0,2)
ax.quiver(x,y,z,Ex,Ey,Ez,color='b',length=1,normalize=True) 
plt.title('E field of a straight wire')
plt.xlabel('x')
plt.ylabel('y')
ax.view_init(elev=-90, azim=90)
plt.show()