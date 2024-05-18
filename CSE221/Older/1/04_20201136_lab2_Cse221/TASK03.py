#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#TASK_03
def rank_students(A,B):
    for i in range(n-1):
        temp=A[i+1]
        temp2=B[i+1]
        j=i
        while j>=0:
            if A[j]<temp:
                A[j+1]=A[j]
                B[j+1]=B[j]
            else: break
            j-=1
        A[j+1]=temp
        B[j+1]=temp2
    return B
    
f=open('input_task03.txt')
lst= [int(x) for x in f.read().split()]
#print(lst)
    
n=lst[0]
id_list=lst[1:n+1]
marks_list=lst[n+1:]

arr=rank_students(marks_list,id_list)
f2=open('output_task03.txt','w')
for i in arr:
    f2.write(str(i)+' ')
f.close()
f2.close()

