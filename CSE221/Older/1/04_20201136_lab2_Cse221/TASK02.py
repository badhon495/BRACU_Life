#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#TASK_02
def selection_sort(A,n):
    for i in range(n):
        m=i
        for j in range(i+1,n):
            if A[j]<A[m]:
                m=j
        A[i],A[m]=A[m],A[i]
    return A
f=(open('input_task02.txt'))
lst=[int(x) for x in f.read().split()]
# print(lst)
N=lst[0]
M=lst[1]
arr=selection_sort(lst[2:],N)
f2=open('output_task02.txt','w')
for i in range(M):
    f2.write(str(arr[i])+' ')
f.close()
f2.close()

