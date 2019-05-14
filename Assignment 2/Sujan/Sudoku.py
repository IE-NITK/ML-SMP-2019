
import numpy as np
n=int(input("enter size"))

mat=np.zeros((n,n))

for i in range(n):
    for j in range(n):
        mat[i][j]=int(input(""))

    
    f=1
for i in range(n):
    if i not in mat[i][:]  or i  not in mat[:][i]:
        f=0
        break
        
        
if(f==1):
    print('sudoku')
        
    

    
        
    
