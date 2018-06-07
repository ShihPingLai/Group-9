## 1. 目的:
要畫出通有表面電流cable的磁場，我們把它看成很多的長直導線排列成一個圓圈，數量越多得到的結果越真實。將每一根長直導線的造成的磁場疊加起來即為結果。
最後呈現的結果是把磁場的向量場畫出來

## 2. 如何使用:

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
