## 電荷在空間中的磁場分佈 #


### 一、目的 
透過使用者輸入不同位置，以python模擬在空間中放入多個電荷後，周圍的2D或3D場分佈圖。


### 二、使用說明:


假設放入電荷的介面為一個在 XY 平面上 3X3 的陣列，可放入 9 個大小不同的電荷：
```n = 3
position = np.zeros([n, n])         #([row, col]) 
``` 

使用者輸入電荷大小（單位：庫倫）至此陣列中，分別依序對應至 9 個位置點：

(x,y)= (0,0), (1,0), (2,0), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)

```
for i in range(0,n):
     for j in range(0,n):
       position[i][j]= input("enter:")
print position
```

在平面上顯示電荷位置（若電荷＝0 不顯示）

```for i in range(0,n):
    for j in range(0,n):
        if position[i][j]==0:
            continue          
        plt.plot([i], [j], [0], color='red', marker='o', markersize=5)
```

個別算出單一電荷周圍之電場大小，及 x,y,z方向分量：

```
 e=8.85*10**-12 
 EE = (1./(4*np.pi*e))*q/((x-m)**2+(y-n)**2+(z-l)**2) 
    Ex=EE*(x-m)/np.sqrt((x-m)**2+(y-n)**2+(z-l)**2)         #Ex: x方向電場
    Ey=EE*(y-n)/np.sqrt((x-m)**2+(y-n)**2+(z-l)**2)         #Ey: y方向電場
    Ez=EE*(z-l)/np.sqrt((x-m)**2+(y-n)**2+(z-l)**2)         #Ez: z方向電場  
```
其中 e 為真空中的介電常數 𝝐0 = 8.85*10^-12。 


以z=0 使2維陣列落在 XY 平面上， 形成以 (i,j,0) 為核心周圍的電場 
```
Ex,Ey,Ez=E(x, y, z, i, j, 0, position[i][j]) 
```

最後，
分別以2D或3D的繪圖方式畫出電場分佈。



### 三、結果

以 plt.quiver 畫出向量圖，箭號大小表示電場大小，箭號方向表示電場方向

# 1. 畫出2D電場分佈圖

假設輸入陣列依序為： 
```
enter:0
enter:5
enter:0
enter:0
enter:0
enter:0
enter:-10
enter:0
enter:0
[[  0.   5.   0.]
 [  0.   0.   0.]
 [-10.   0.   0.]]
 ```
 
 



