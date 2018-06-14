## 電荷在空間中的磁場分佈 #


### 一、目的 
透過使用者輸入不同位置，以python模擬在空間中放入多個電荷後，周圍的2D或3D場分佈圖。


### 二、使用說明:

1. 輸入介面為 2D 平面

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


2. 輸入介面為 3D 空間

與2D電場程式相似，唯一的差別在於，由於輸到了三維空間，若要一一輸入3*3*3=27個座標點上電荷的有無與大小將相當費時，因此改良為由使用者輸入所要放入電場的電荷數量、電荷大小/正負與指定的座標。

設定一個 3X3X3 的三維陣列：
```
n = 3 
position = np.zeros([n, n, n])
```

先輸入想要放置的電荷數：
```
no_of_charges = input("Enter the number of charges you want:")
while no_of_charges <=0:
    print "There must be at least one charge to generate an electric field!"
    no_of_charges = input("Enter the number of charges you want:")
```

依序輸入該電荷的 (x,y,z)座標 與 電荷大小：
```
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
```
最後畫出電場分佈圖。


就整體討論而言，2D輸入與3D輸入電場有相同缺點，因為是由陣列來表示座標點的位置，無法將點電荷放到座標為0與2以外的點上，也無法放到非整數的位置；

但大體上已經達到將所指定電場(疊加)分布視覺化的功能了。


### 三、結果

以 plt.quiver 畫出向量圖，箭號大小表示電場大小，箭號方向表示電場方向

1. 畫出二維輸入介面的電場分佈

- 2D電場分佈

使用程式 [E Field with user 2D input (2D)](https://github.com/ShihPingLai/Group-9/blob/master/E%20field/E%20Field%20with%20user%20%202D%20input%20(2D).py) 

假設以下依序為輸入陣列，可得到結果如下圖： 
```
enter:0         
enter:5         #位置為(0,1)，所帶電荷為+5
enter:0
enter:0
enter:0
enter:0
enter:-10       #位置為(2,0)，所帶電荷為-10
enter:0
enter:0
[[  0.   5.   0.]
 [  0.   0.   0.]
 [-10.   0.   0.]]
 ```
 ![Alt text](https://raw.githubusercontent.com/ShihPingLai/Group-9/master/E%20field/figure/E%20with%202D%20input%20(2D)%20.png)

 
- 3D電場分佈

使用程式[E Field with user 2D input (3D)](https://github.com/ShihPingLai/Group-9/blob/master/E%20field/E%20Field%20with%20user%202D%20input%20(3D).py) 

假設以下依序為輸入陣列，可得到結果如下圖： 
```
enter:5            #位置為(0,0)，所帶電荷為+5
enter:0
enter:0
enter:0
enter:0
enter:0
enter:0
enter:0
enter:-10          #位置為(2,2)，所帶電荷為-10
[[  5.   0.   0.]
 [  0.   0.   0.]
 [  0.   0. -10.]]
```
 ![Alt text](https://raw.githubusercontent.com/ShihPingLai/Group-9/master/E%20field/figure/E%20with%202D%20input%20(3D)%20.png)
 
 
2. 畫出三維輸入介面的電場分佈

使用程式[E Field with user 3D input (3D)](https://github.com/ShihPingLai/Group-9/blob/master/E%20field/E%20field%20with%20user%203D%20input.py) 

- 先輸入想要放置的電荷數（以下放入3電荷為例）：
```
Enter the number of charges you want:0
There must be at least one charge to generate an electric field!
```
若當輸入的電荷<=0時，將要求使用者重新輸入，直到電荷數不為零。
```Enter the number of charges you want:3  ```

- 分別輸入電荷資訊：

在 (0,0,0) 和 (2,2,0) 放入帶電量為 +5 的電荷

在 (1,1,2) 放入帶電量為 -10 的電荷
```enter x coordinate, 0<=x<3, x=integer:0
enter y coordinate, 0<=y<3, y=integer:0
enter z coordinate, 0<=z<3, z=integer:0
enter the magnitude of the charge:5
A charge of magnitude 5 is placed at coordinate 0 0 0
enter x coordinate, 0<=x<3, x=integer:2
enter y coordinate, 0<=y<3, y=integer:2
enter z coordinate, 0<=z<3, z=integer:0
enter the magnitude of the charge:5
A charge of magnitude 5 is placed at coordinate 2 2 0
enter x coordinate, 0<=x<3, x=integer:1
enter y coordinate, 0<=y<3, y=integer:1
enter z coordinate, 0<=z<3, z=integer:2
enter the magnitude of the charge:-10
A charge of magnitude -10 is placed at coordinate 1 1 2
```
可以得到以下結果
 ![Alt text](https://raw.githubusercontent.com/ShihPingLai/Group-9/master/E%20field/figure/E%20with%203D%20input%20(3D)%20.png)
