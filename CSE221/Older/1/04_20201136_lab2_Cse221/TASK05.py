#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#TASK_05
def QUICKSORT(A,p,r):
    if p<r:
        q = partition(A,p,r)
        QUICKSORT(A,p,q-1)
        QUICKSORT(A,q+1,r)

def partition(array,p,q):
    x = A[p]
    i = p
    for j in range(p+1,q+1):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]

    A[p],A[i] = A[i],A[p]
    return i
A=[2,1,5,5,9,3,7,8,0]
QUICKSORT(A,0,len(A)-1)

def findK(A,start,end,k):
    while start<=end:
        if k < end and k < 1:
            return -1
        else:
            i = partition(A,start,end)
            if i > k-1:
                end = i-1
            else:
                if i < k-1:
                    start = i+1
                else:
                    return A[i]
A=[1,3,4,5,9,10,10]                
print(findK(A,0,len(A)-1,5))

