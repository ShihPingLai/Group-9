
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3,4,20)
y = np.linspace(-3,4,20)
x,y = np.meshgrid(x,y)

# 2d figure
fig = plt.figure()
ax = fig.add_subplot(111)  #畫出2維的座標軸

def E(x,y,m,n,q):     
    e=8.85*10**-12           
    EE = (1./(4*np.pi*e))*q/((x-m)**2+(y-n)**2)    #Magnitude of the vector E 磁場
    Ex=EE*(np.cos(np.arctan2(y-n,x-m)))            #Ey: y方向電場 arctan2(y,x)是反tan(x/y)
    Ey=EE*(np.sin(np.arctan2(y-n,x-m)))            #Ex: x方向電場
 
    return Ex,Ey

#initialise
ex = 0
ey = 0

n = 3 
position = np.zeros([n, n]) # ([row, col])
# print position

for i in range(0,n):
    for j in range(0,n):
       position[i][j]= input("enter:")
print position

for i in range(0,n):
    for j in range(0,n):
        if position[i][j]==0:
            continue          
            
        Ex, Ey =E(x, y, i, j, position[i][j])
        ex = Ex + ex
        ey = Ey + ey
        
        plt.plot([i], [j], color='red', marker='o', markersize=5)   
    
plt.quiver(x,y,ex,ey,width=0.03,units='xy',color='b', scale = 30000000000)
        
plt.title('E field of positive charges with user 2D input (2D)')
plt.xlabel('x')
plt.ylabel('y')
#ax.view_init(elev=-90, azim=90)


    
plt.show()

