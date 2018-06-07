# Creat_Magnetic_Field_User.ipynb #
## 目的 ##
此程式的目的為，使用者可自行指定在不同位置放上不同大小的磁鐵，程式會跑出這些磁鐵產生的磁力線分布。

## 程式說明 ##
### 1.建構小磁鐵 ###
```
    half_L = 0.5              #螺線管長度的一半
    N = 100                   #單位長度的匝數
    r = 1                     #螺線管半徑   
```
### 輸入說明: 以預設值為例 ###
程式預設為: 使用者可在空間中x,y,z = 0,1,2的範圍內，自由選擇磁鐵放置的位置與磁鐵大小。   
程式會要求使用者輸入27個數值,分別代表上述範圍的27個點對應到的磁鐵大小。   
磁鐵大小的單位為安培(A)   
註: 程式中以一個短螺線管代表一個小磁鐵，所以磁鐵的大小由螺線管的電流決定。   
    電流=0 代表此位置不放磁鐵

27個位置依序代表:   

(x, y, z)=   
1. (0,0,0) &nbsp; &nbsp; &nbsp; 10. (0,1,0) &nbsp; &nbsp; &nbsp; 19. (0,2,0)   
2. (0,0,1) &nbsp; &nbsp; &nbsp; 11. (0,1,1) &nbsp; &nbsp; &nbsp; 20. (0,2,1)   
3. (0,0,2) &nbsp; &nbsp; &nbsp; 12. (0,1,2) &nbsp; &nbsp; &nbsp; 21. (0,2,2)   
4. (1,0,0) &nbsp; &nbsp; &nbsp; 13. (1,1,0) &nbsp; &nbsp; &nbsp; 22. (1,2,0)   
5. (1,0,1) &nbsp; &nbsp; &nbsp; 14. (1,1,1) &nbsp; &nbsp; &nbsp; 23. (1,2,1)   
6. (1,0,2) &nbsp; &nbsp; &nbsp; 15. (1,1,2) &nbsp; &nbsp; &nbsp; 24. (1,2,2)   
7. (2,0,0) &nbsp; &nbsp; &nbsp; 16. (2,1,0) &nbsp; &nbsp; &nbsp; 25. (2,2,0)   
8. (2,0,1) &nbsp; &nbsp; &nbsp; 17. (2,1,1) &nbsp; &nbsp; &nbsp; 26. (2,2,1)   
9. (2,0,2) &nbsp; &nbsp; &nbsp; 18. (2,1,2) &nbsp; &nbsp; &nbsp; 27. (2,2,2)   


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


