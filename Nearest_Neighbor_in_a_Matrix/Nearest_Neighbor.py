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
        

    
