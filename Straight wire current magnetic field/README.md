# 1. 目標
完成一作業系統可讓使用者任意輸入欲分布之長直導線的圖形
> 第一部分-長直導線磁場分布 

**先由網路上抓到單根長直導線磁場分布的code後，將其延伸至多根長直導線**

_方法: 導入位置座標系(矩陣的概念)，可簡化問題_

> 第二部分-使用者輸入  

**思考可變更的參數有哪些** 

_方法:以客製化矩陣供使用者輸入，並自由給定每根長直導線的電流大小_
# 2. 程式流程
step 1:利用meshgrid建立三維立體圖
```
   # 給定x,y,z的範圍(-4與4間取10個數據點)
x = np.linspace(-4,4,10)
y = np.linspace(-4,4,10)
z = np.linspace(-4,4,10)

# 建立3D圖的採樣點
x,y,z = np.meshgrid(x,y,z)

# 建立3D圖
fig = plt.figure(figsize=(12,12))
ax = fig.gca(projection='3d')
```
step 2:定義磁場大小與直導線位置
```
# 加入導線位置(m,n),相對座標變為(x-m,y-n)
def B(x,y,m,n):
    i = 1                                           #Amps in the wire
    mu = 1.26 * 10**(-6)                            #Magnetic constant    (H/m)                   
    mag = (mu/(2*np.pi))*(i/np.sqrt((x-m)**2+(y-n)**2)) #Magnitude of the vector B 磁場
    by = mag * (np.cos(np.arctan2(y-n,x-m)))            #By y方向磁場 arctan2(y,x)是反tan(x/y)
    bx = mag * (-np.sin(np.arctan2(y-n,x-m)))           #Bx x方向磁場
    bz = z*0                                        #Bz (zero, using the right-hand rule)
    return bx,by,bz

def cylinder(r,m,n):   #m,n是導線的位置
    phi = np.linspace(-np.pi,np.pi,100)
    x = m+r*np.cos(phi) # +m更正
    y = n+r*np.sin(phi) # +n更正
    return x,y
```
> 磁場部分:利用直導線磁場公式B=M0*I/2*pi*r 其中r=((x-m)^2+(y-n)^2)^(1/2) m,n為導線位置 bx,by,bz分別為磁場的x,y,z分量

> 導線部分:建立一個圓柱並輸出x,y分量
step 3:使用者輸入
```
# 給定磁場初始值
Bx=0
By=0
Bz=0

# 建立一3*3矩陣,數值由使用者輸入
n = 3
position = np.zeros([n, n]) # ([row, col])  #使用者輸入,由(1,1)至(3,3)共9個位置
for i in range(0,n):
    for j in range(0,n):
        position[i][j]= input("enter:")
print(position) #顯示矩陣

#建立磁場與導線
for i in range(0,n):
    for j in range(0,n):
        if position[i][j]==0: # 若使用者輸入為0,則略過
            continue
        bx,by,bz = B(x,y,i,j)           #Magnetic field
        Bx=Bx+bx                        #+bx修正
        By=By+by                        #+by修正    
        Bz=Bz+bz                        #+bz修正
        cx,cy = cylinder(0.2,i,j)       #Wire
        for l in np.linspace(-4,4,800):  #-4到4是指線的長度,總長8    #Plot the wire
            ax.plot(cx,cy,l,label='Cylinder',color='r') 
```
導線位置與電流大小由使用者決定，分別輸入3*3中的9個位置
# 3. 使用說明
畫面會先出現一個輸入介面enter，此介面將會出現9次，分別是長直導線可作用的九個位置，順序為左到右，上到下
# 4. 結果
| current position  | magnetic field contribution |
| :---------------- |----------------------------:|
| [[ 4.  0.  0.][ 0.  5.  5.][ 3.  0.  2.]] | ![Alt text](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/34479224_1750927958321387_1250771386574569472_n.png?_nc_cat=0&oh=90c9306ba042d3e80bde9ccbba17aab4&oe=5BB91CC3) | 
| [[ 1.  0.  6.][ 0.  0.  8.][ 9.  7.  2.]] | ![Alt text](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/34822100_1750931124987737_7275885512383004672_n.png?_nc_cat=0&oh=eb6f836f30ed92203f44bd0e1829da0b&oe=5BAE11AF) | 
| [[ 1.  0.  0.][ 0.  0.  1.][ 0.  1.  0.]] | ![Alt text](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/34667660_1750931131654403_8962445729876410368_n.png?_nc_cat=0&oh=52029c3d11945e8ee9b0229486dc14c7&oe=5BAFB908) |
# 5. 最終版程式名稱
final results
