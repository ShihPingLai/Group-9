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
> 磁場部分:利用直導線磁場公式B=M0*I/2*pi*r 其中r=((x-m)^2+(y-n)^2)^(1/2) m,n為導線位置 bx,by,bz分別為磁場的x,y,z分量 這裡的電流值i固定為1

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
        Bx=(Bx+bx*position[i][j])*50    #+bx*position修正(電流變幾倍磁場就變幾倍)
        By=(By+by*position[i][j])*50    #+by*position修正(電流變幾倍磁場就變幾倍) 
        #乘上50是為了在圖形的結果能看得見
        Bz=Bz+bz                        #+bz修正
        cx,cy = cylinder(0.2,i,j)       #Wire
        for l in np.linspace(-4,4,800):  #-4到4是指線的長度,總長8    #Plot the wire
            ax.plot(cx,cy,l,label='Cylinder',color='r') 
            
```
導線位置與電流大小由使用者決定，分別輸入3*3中的9個位置

step 4:畫圖
# 3. 使用說明
畫面會先出現一個輸入介面enter，此介面將會出現9次，分別是長直導線可作用的九個位置，順序為左到右，上到下
# 4. 結果
| current position  | magnetic field contribution |
| :---------------- |----------------------------:|
| [[1. 0. 2.][0. 0. 0.][3. 0. 4.]] | ![Alt text](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-0/s370x247/35079438_1758285814252268_3130704947427934208_n.png?_nc_cat=0&oh=f6cc212189da878843f81a38f3317662&oe=5B7920FB) | 
| [[1. 2. 3.][4. 0. 0.][0. 0. 0.]] | ![Alt text](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/35166839_1758285810918935_693702604886114304_n.png?_nc_cat=0&oh=07ee1da38917197f8d05e21afdb9622d&oe=5BB45DF2) | 
| [[     0.      0.      0.][     0. 100000.      0.][     0.      0.      0.]] | ![Alt text](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-0/s370x247/35180975_1758285800918936_9114190858634133504_n.png?_nc_cat=0&oh=fa86d3bda3151a2385c4feaae0e5d107&oe=5BB8D5A8) |
# 5. 最終版程式名稱
final result 2
