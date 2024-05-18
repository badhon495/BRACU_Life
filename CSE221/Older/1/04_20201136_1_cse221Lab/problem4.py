#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TASK 4
import numpy as np
file=open('matrix_input.txt')
file2=open('matrix_output.txt','w')
lst=file.readlines()
n=int(lst[0].strip())
A=[]
B=[]
for i in lst[1:n+1]:
    for j in i.strip():
        if j!=' ':
            A+=[int(j)]
            
for x in lst[n+1:]:
    for y in x.strip():
        if y!=' ':
            B+=[int(y)]
    
A=np.array(A)
A=A.reshape(n,n)
B=np.array(B)
B=B.reshape(n,n)

C=np.array([0]*n*n)
C=C.reshape(n,n)
for i in range(n-1):
    for j in range(n-1):
        for k in range(n-1):
            C[i,j] += A[i,k]*B[k,j]  

C=np.array([0]*(n*n))
C=C.reshape(n,n)
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i,j] += A[i,k]*B[k,j]  
# print(lst)
print(A)
print(B)
print(C)
file2.write(str(C))
file.close()
file2.close()


# In[ ]:




