#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#TASK_04
def MERGE(A,l,m,r):
    n1=m-l+1
    n2=r-m
    L=[0]*(n1+1)
    R=[0]*(n2+1)
    
    for i in range(n1+1):
        L[i]=A[l+i]

    
    for j in range(n2):  
        R[j]=A[m+j+1]
        
    i=j=0
    x=l
    for k in range(l,r): 
        if i<n1 and j<n2:
            if L[i]<=R[j]:

                A[k]=L[i]
                i+=1
            else:
                A[k]=R[j]
                j+=1
            x+=1
       
   
    while i < n1:
        A[x] = L[i]
        i += 1
        x+= 1

    while j < n2:
        A[x] = R[j]
        j += 1
        x+= 1
    
def MERGE_SORT(A,l,r):
    if l<r:
        m=(l+r)//2
        MERGE_SORT(A,l,m)
        MERGE_SORT(A,m+1,r)
        MERGE(A,l,m,r)
    return A

f=open('input_task04.txt')
lst= [int(x) for x in f.read().split()]
A=MERGE_SORT(lst[1:],0,lst[0]-1)
f2=open('output_task04.txt','w')
for i in A:
    f2.write(str(i)+' ')
f.close()
f2.close()

