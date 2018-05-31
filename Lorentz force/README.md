## 1. 目的:
由於電荷會受到勞倫茲力而開始運動，但若是電場和磁場不是個定值而是會隨著位置不同而改變的話，用紙筆計算其實有點難想像它的運動軌跡。因此我們利用python，
幫我們畫出電荷的運動軌跡，而電磁場是位置x,y,z的函數

## 2. 如何使用:
首先是決定電荷的初始條件:
```
X=np.array([-5,2,3])
v=np.array([0,3,0])
M=1
Q=1
```
X為電荷的初始位置，v是初始速度，M是電荷質量，Q是電荷大小

在我附的檔案中，共有3個類型: 電磁場固定，磁場是位置的函數，電磁場都是位置的函數
(1)電磁場固定: 
```
 B=np.array([1,0,0]) 
 E=np.array([0,1,0]) 
 ```
上面的意思為: 磁場B在x的分量為1，其餘為0；磁場E在y的分量為1，其餘為0；
所以使用者可自行更改array內x,y,z各分向的電磁場大小

再來要畫出電荷的路徑:
```
for t in range(0,2000):
    F=Q*E+Q*(np.cross(v,B))
    a=F/M
    v=v+a*0.01  
    X=X+v*0.01  
```
a是加速度，F是勞倫茲力。上面意思是每0.01秒紀錄一個點的位置，這0.01秒內，由於時間很短，所以同一區間的速度和加速度可視為定值。如果想要更精細的話時間尺度改短一點即可。

(2)磁場是位置的函數:
```
for t in range(0,200):
    def B(x,y,z):
        B=np.array([x*y,0,0])  
        return B
    B=B(X[0],X[1],X[2])
    F=Q*E+Q*(np.cross(v,B))
    a=F/M
    v=v+a*0.01
    X=X+v*0.01
```
上面的意思為: 磁場B在x的分量為那點位置的x和y相乘，其餘方向為0。使用者可自行決定B的函數

(3)電磁場都是位置的函數:
```
for t in range(0,200):
    def B(x,y,z):
        B=np.array([x*y,0,0])
        return B
    B=B(X[0],X[1],X[2])
    def E(x,y,z):
        E=np.array([y/x,0,x*z]) #電場是位置的函數
        return E
    E=E(X[0],X[1],X[2])
    
    F=Q*E+Q*(np.cross(v,B))
    a=F/M
    v=v+a*0.01
    X=X+v*0.01
```
電場也變成位置的函數，使用者可自行決定E、B的函數

最後，使用者可以從各個方向來觀看路徑:
```
ax.view_init(elev=40, azim=-80)    
```
elev是仰角，azim是沿z軸旋轉。

畫出路徑:
```
ax.scatter(Y1,Y2,Y3,marker='o', color="red")     
```
marker的大小顏色也可以改變

## 3. 畫圖結果:
(1)電磁場固定:
```
 B=np.array([1,0,0]) 
 E=np.array([0,1,0]) 
 ```
 https://github.com/ShihPingLai/Group-9/blob/master/Lorentz%20force/1.png
 
 
