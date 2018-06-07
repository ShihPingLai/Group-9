## 1. 目的:
要畫出通有表面電流cable的磁場，我們把它看成很多的長直導線排列成一個圓圈，數量越多得到的結果越真實。將每一根長直導線的造成的磁場疊加起來即為結果。
最後呈現的結果是把磁場的向量場畫出來

## 2. 如何使用:

step1: 定義一根無線長直導線的所造成的磁場
```
def B(x,y,m,n):
    i = 1                                           #current in the wire
    mu = 1.26 * 10**(-6)                            #Magnetic constant    (H/m)                   
    mag = (mu/(2*np.pi))*(i/np.sqrt((x-m)**2+(y-n)**2)) #Magnitude of the vector B 磁場
    by = mag * (np.cos(np.arctan2(y-n,x-m)))            #By y方向磁場 arctan2(y,x)是反tan(x/y)
    bx = mag * (-np.sin(np.arctan2(y-n,x-m)))           #Bx x方向磁場
    bz = z*0                                        #Bz (zero, using the right-hand rule)
    return bx,by,bz
```
我們採用的公式為B=mu*i/(2*pi*r)，r是各點(x,y)和長直導線的距離，你可以改變導線的電流i 。

step2: 畫出長直導線
```
def cylinder(r,m,n):   
    phi = np.linspace(-np.pi,np.pi,100)
    x = m+r*np.cos(phi)
    y = n+r*np.sin(phi)
    return x,y
```
m,n是導線的所在位置，r是導線半徑，把長直導線畫出來。這裡沒什麼物理意義，只是把導線圖像化好方便使用者想像

step3: 把所有直導線的磁場疊加起來
```
Bx=0
By=0
Bz=0
angles = np.linspace(-np.pi, np.pi, 20)  #有20根長直導線
R=3   #導管半徑
for i in angles:
    # Plot of the fields
    bx,by,bz = B(x,y,R*np.cos(i),R*np.sin(i))  #Magnetic field
    Bx=Bx+bx
    By=By+by
    Bz=Bz+bz
    cx,cy = cylinder(0.1,R*np.cos(i),R*np.sin(i))                             
    for j in np.linspace(-4,4,800):  #-4到4是指線的長度，在4到4之間畫800個點  Plot the wire
        ax.plot(cx,cy,j,label='Cylinder',color='r') 
ax.quiver(x,y,z,Bx,By,Bz,color='b',length=0.5,normalize=True)  #畫B的vector
```
angles是指把很多的長直導線排列成圓環，來近似一個同軸電纜的磁場，linspace的分割數目即為用幾根導線排列成環
R是同軸電纜的半徑。利用for loop把每一根導線的磁場疊加到Bx、By、Bz，並畫出導線。導線的位置為(R*np.cos(i),R*np.sin(i))
，半徑=0.1。
在 for j in np.linspace(-4,4,800)，意思是在-4到4之間畫出800個點，因為很密集，所以看起來像一根線
最後再用ax.quiver把磁場畫出來，可以改變vector的color和length。

## 3. 結果:
結果其實有點不如我意，這個圖形不是圓對稱，雖然已修改多次，包括增加導線數目讓結果更真實，但也不知道為什麼不對稱。
另外我也發現到，在angles = np.linspace(-np.pi, np.pi, 20)，原本是從-180度畫到180度，若改為從0畫到360度，出來的圖形會不同，所以代表這跟畫圖的方向有關。不過我覺得很奇怪，應該是要沒差才對。
![Alt text](https://github.com/ShihPingLai/Group-9/blob/master/B%20field%20of%20cable/fig1.png)
fig1: -180度畫到180度
![Alt text](https://github.com/ShihPingLai/Group-9/blob/master/B%20field%20of%20cable/fig2.png)
fig2: 0度畫到360度

## 4. 延伸:同軸電纜的磁場
在剛剛的電纜裡面再加一根導線，電流方向相反，即為同軸電纜
```
dx,dy=cylinder(0.1,0,0)   
for j in np.linspace(-4,4,800):
    ax.plot(dx,dy,j,label='Cylinder',color='g')  #導管內部又放一根長直導線
Dx,Dy,Dz = B(x,y,0,0) 
ax.quiver(x,y,z,Bx-Dx,By-Dy,Bz-Dz,color='b',length=0.5,normalize=True)  #畫B的vector
```
我設它的位置在(0,0)，半徑=0.1。Dx,Dy,Dz是它產生的磁場，但因為電流方向和外面電纜相反，故最後畫磁場是(Bx-Dx,By-Dy,Bz-Dz)。
一樣結果超奇怪，但我還是找不出問題，失敗的作品QQ
![Alt text](https://github.com/ShihPingLai/Group-9/blob/master/B%20field%20of%20cable/fig3.png)
fig3: 同軸電纜
