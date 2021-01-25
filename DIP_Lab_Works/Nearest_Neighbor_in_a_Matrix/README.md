**Finding Nearest Neigbor of each element in a Matrix and sum of Nearest Neigbor**

```python
#multi-D array
r,c=int(input("Enter Array size:\nrows= ")),int(input("cols= "))
arr=[[int(input('arr['+str(i)+']['+str(j)+']= ')) for j in range(c)] for i in range(r)]
print(str(r)+'x'+str(c)+" Array:",*arr,sep='\n')


import numpy as np
nparr=np.array(arr)
type(nparr)

for m in range(nparr.shape[0]):
        for n in range(nparr.shape[1]):
            sum=0    
            print("Nearest Neighbors of {0} at ({1},{2}):".format(nparr[m][n],m,n))
            Lm,Ln=m,n-1
            if (Ln>=0): 
                L=nparr[Lm][Ln]
                print("Left= ",L)
                sum+=L

            Tm,Tn=m-1,n
            if Tm>=0:
                T=nparr[Tm][Tn]
                print("Top=",T)
                sum+=T

            Rm,Rn=m,n+1
            if(Rn<nparr.shape[1]):
                R=nparr[Rm][Rn]
                print("Right= ",R)
                sum+=R

            Bm,Bn=m+1,n
            if Bm<nparr.shape[0]:
                B=nparr[Bm][Bn]
                print("Bottom=", B)
                sum+=B

            print("sum of Neighbors= ",sum,end="\n\n")
```
output:
```
>>> 
======= RESTART: C:\Users\Sanjay-PC\DIP\DIP_Lab_Works\Nearest_Neighbor.py ======
Enter Array size:
rows= 3
cols= 3
arr[0][0]= 80
arr[0][1]= 70
arr[0][2]= 90
arr[1][0]= 60
arr[1][1]= 50
arr[1][2]= 40
arr[2][0]= 30
arr[2][1]= 10
arr[2][2]= 20
3x3 Array:
[80, 70, 90]
[60, 50, 40]
[30, 10, 20]
Nearest Neighbors of 80 at (0,0):
Right=  70
Bottom= 60
sum of Neighbors=  130

Nearest Neighbors of 70 at (0,1):
Left=  80
Right=  90
Bottom= 50
sum of Neighbors=  220

Nearest Neighbors of 90 at (0,2):
Left=  70
Bottom= 40
sum of Neighbors=  110

Nearest Neighbors of 60 at (1,0):
Top= 80
Right=  50
Bottom= 30
sum of Neighbors=  160

Nearest Neighbors of 50 at (1,1):
Left=  60
Top= 70
Right=  40
Bottom= 10
sum of Neighbors=  180

Nearest Neighbors of 40 at (1,2):
Left=  50
Top= 90
Bottom= 20
sum of Neighbors=  160

Nearest Neighbors of 30 at (2,0):
Top= 60
Right=  10
sum of Neighbors=  70

Nearest Neighbors of 10 at (2,1):
Left=  30
Top= 50
Right=  20
sum of Neighbors=  100

Nearest Neighbors of 20 at (2,2):
Left=  10
Top= 40
sum of Neighbors=  50
```

    
