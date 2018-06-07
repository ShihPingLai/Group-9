# Creat_Magnetic_Field_User.ipynb #
## 目的 ##
此程式的目的為，使用者可自行指定在不同位置放上不同大小的磁鐵，程式會跑出這些磁鐵產生的磁力線分布。

## 程式說明 ##
### 1.建構小磁鐵 ###
```
    half_L = 0.5              #螺線管長度的一半
    N = 100                   #單位長度的匝數
    r = 1                     #螺線管半徑   
       
    def cylinder(r,m,n,l):    
    phi = np.linspace(-2*np.pi,2*np.pi,100)
    xp = m + r*np.cos(phi)
    yp = n + r*np.sin(phi)
    zp = l + np.linspace(-half_L,half_L,N)
    return xp, yp, zp
```   
在程式中每個小磁鐵都以短螺線管表示，因此要設定螺線管的基本性質(長度、半徑、匝數)。   
函數cylinder用來決定小磁鐵在空間中的位置:   
(m,n,l)代表螺線管中心點的座標位置，r是螺線管半徑    
函數return的值為螺線管每個點的x,y,z座標   
   
### 2.如何讓使用者輸入放置磁鐵的位置 ###
```
    n = 3
    position = np.zeros([n, n, n]) # ([row, col])  #使用者輸入
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                position[i][j][k]= input("enter:")
                current = position[i][j][k]        #電流
    print(position)
```
position為一個n x n x n的空間，也就是包含所有x,y,z = 0 ~ n-1 的格子點。   
position[i][j][k]則代表(x,y,z) = (i,j,k)這個點上的磁鐵大小，也就是中心點在(i,j,k)的螺線管電流大小。 
註:程式預設的n=3，代表使用者只能在x,y,z = 0~2 範圍內的格子點放置磁鐵   
   
### 3.建立磁場 ###   
```
#算出一小段螺線管造成的磁場
def dB(x, y, z, theta, zp, m, n, l):
    
    dbx = mu*current*r/4/np.pi*(z-zp)*np.cos(theta)/((x-m)**2+(y-n)**2+(z-zp)**2+r**2-2*r*((x-m)*np.cos(theta)+(y-    n)*np.sin(theta)))**1.5

    dby = mu*current*r/4/np.pi*(z-zp)*np.sin(theta)/((x-m)**2+(y-n)**2+(z-zp)**2+r**2-2*r*((x-m)*np.cos(theta)+(y-n)*np.sin(theta)))**1.5

    dbz = mu*current*r/4/np.pi*(1 - ((x-m)*np.cos(theta)+(y-n)*np.sin(theta)))/((x-m)**2+(y-n)**2+(z-zp)**2+r**2-2*r*((x-m)*np.cos(theta)+(y-n)*np.sin(theta)))**1.5
    
    return dbx, dby, dbz
```   
將螺線管看成許多圓環密集疊加而成。此處dB的功能為算出一個圓環的一小部分對空間中一點(x,y,z)造成的磁場。  
dB中變數的意義:   
(x,y,z)代表要計算磁場那個點的座標，(m,n,l)代表螺線管中心的座標，zp代表螺線管中某個圓環的中心座標。   
將圓環上的每個小部分以極座標表示(r,theta)表示，r為螺線管的半徑。   
   
```   
#將每一段螺線管的貢獻加總 

   theta = np.linspace(0,2*np.pi,100)                #以theta描述螺線管每一段的位置


   bx = np.zeros((spacing,spacing,spacing))          
   by = np.zeros((spacing,spacing,spacing))
   bz = np.zeros((spacing,spacing,spacing))


   for i in range(0,n):
       for j in range(0,n):
           for k in range(0,n):
               cx,cy,cz = cylinder(1,i,j,k)         #cz代表每個環的位置
               for p in cz:
                   for t in theta:
                       if position[i][j][k]==0:
                           continue
                       bx += dB(x, y, z, t, p, i, j, k)[0]
                       by += dB(x, y, z, t, p, i, j, k)[1]
                       bz += dB(x, y, z, t, p, i, j, k)[2]
```   
dB已經算出螺線管的某個小部分貢獻的磁場，而此部分則要將所有小部分的貢獻加總，變成整個螺線管對空間中一點(x,y,z)造成的磁場。   
將dB對theta加總可得到一個圓環的貢獻，對zp加總可得到一個螺線管的貢獻。   
對m、n、l加總可得到所有螺線管的貢獻，加總範圍為position內的空間。若position[i][j][k]=0，則該點無貢獻任何磁場，代表該點無放置磁鐵。 
   
### 4.畫出磁場分布圖 ###
``` 
# Plot of the 3d vector field
ax.quiver(x,y,z,bx,by,bz,color='b',length=1,normalize=True)
``` 
ax.quiver可使磁力線的分布以向量表示   
   
### 輸入說明: 以預設值為例 ###   
程式預設為: 使用者可在空間中x,y,z = 0,1,2的範圍內，自由選擇磁鐵放置的位置與磁鐵大小。   
程式會要求使用者輸入27個數值,分別代表上述範圍的27個點對應到的磁鐵大小。   
磁鐵大小的單位為安培(A)   
註: 程式中以一個短螺線管代表一個小磁鐵，所以磁鐵的大小由螺線管的電流決定。   
    電流=0 代表此位置不放磁鐵

27個位置依序代表:   
```
(x, y, z)=   
1. (0,0,0)    10. (0,1,0)    19. (0,2,0)   
2. (0,0,1)    11. (0,1,1)    20. (0,2,1)   
3. (0,0,2)    12. (0,1,2)    21. (0,2,2)   
4. (1,0,0)    13. (1,1,0)    22. (1,2,0)   
5. (1,0,1)    14. (1,1,1)    23. (1,2,1)   
6. (1,0,2)    15. (1,1,2)    24. (1,2,2)   
7. (2,0,0)    16. (2,1,0)    25. (2,2,0)   
8. (2,0,1)    17. (2,1,1)    26. (2,2,1)   
9. (2,0,2)    18. (2,1,2)    27. (2,2,2)   
```

## EXAMPLE ##  
### Example1: ###
若想在(0, 0, 0)及(2, 2, 2)兩位置各放上一個電流為1A的磁鐵，則輸入形式為:   
      
![Alt text](https://raw.githubusercontent.com/ShihPingLai/Group-9/master/B_Field/%E8%BC%B8%E5%85%A5%E8%AA%AA%E6%98%8E.png "figure1")   
   
跑出的結果:    
![Alt text](https://raw.githubusercontent.com/ShihPingLai/Group-9/master/B_Field/figure1.png "figure1")   
Figure1: 在(0, 0, 0)及(2, 2, 2)兩位置放上電流為1A的磁鐵形成的磁力線分布  
   
### Example2: ###
在27個位置上都放上磁鐵   
   
![Alt text](https://raw.githubusercontent.com/ShihPingLai/Group-9/master/B_Field/figure2.png "figure2")     
Figure2: 在27個位置上都放置電流大小不等的磁鐵   


