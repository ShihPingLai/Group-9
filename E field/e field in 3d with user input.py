# -*- coding: utf-8 -*-
## E field of a positive charge in 3D

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,4,6)   #以6個向量標示
y = np.linspace(0,4,6)
z = np.linspace(0,4,6)
x,y,z = np.meshgrid(x,y,z)

# 3d figure
fig = plt.figure()
ax = fig.gca(projection='3d')  #畫出3維的座標軸
ax.view_init(elev=30, azim = 0)

def E(x,y,z,m,n,l,q):     
    e=8.85*10**-12           
    EE = (1./(4*np.pi*e))*q/((x-m)**2+(y-n)**2+(z-l)**2) #Magnitude of the vector  電場
    Ex=EE*(x-m)/np.sqrt((x-m)**2+(y-n)**2+(z-l)**2)         #Ex: x方向電場 arctan2(y,x)是反tan(x/y)
    Ey=EE*(y-n)/np.sqrt((x-m)**2+(y-n)**2+(z-l)**2)         #Ey: y方向電場
    Ez=EE*(z-l)/np.sqrt((x-m)**2+(y-n)**2+(z-l)**2)         #Ez: z方向電場  
    return Ex,Ey,Ez


#initialise
ex = 0
ey = 0
ez = 0

n = 3 
position = np.zeros([n, n, n]) # ([row, col])

no_of_charges = input("Enter the number of charges you want:")
while no_of_charges <=0:
    print "There must be at least one charge to generate an electric field!"
    no_of_charges = input("Enter the number of charges you want:")

    
for w in range(no_of_charges):
    a = input("enter x coordinate, 0<=x<3, x=integer:")
    b = input("enter y coordinate, 0<=y<3, y=integer:")
    c = input("enter z coordinate, 0<=z<3, z=integer:")
    mag = input("enter the magnitude of the charge:")
    position[a][b][c] = mag
    print("A charge of magnitude"),
    print mag,
    print "is placed at coordinate",
    print  a, b, c

   
for i in range(0,n):
    for j in range(0,n):
        for k in range(0, n):
            if position[i][j][k]==0:
                continue          
            Ex,Ey,Ez=E(x, y, z, i, j, k, position[i][j][k])
            ex=Ex+ex
            ey=Ey+ey
            ez=Ez+ez
            plt.plot([i], [j], [k], color='red', marker='o', markersize=5) 

     

ax.quiver(x,y,z,ex,ey,ez,color='b',length=1,normalize=True) 
plt.title('E field of a positive charge')
plt.xlabel('x')
plt.ylabel('y')
plt.ylabel('z')
plt.plot
plt.show()




#for angle in range(0, 360):
    #ax.view_init(30,angle)
    
plt.show()