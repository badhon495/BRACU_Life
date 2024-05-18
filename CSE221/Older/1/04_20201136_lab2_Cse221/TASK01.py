#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#TASK_01
def bubbleSort(arr):
    if_sorted=True
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                if_sorted=False
        if if_sorted==True:
            return arr
    return arr
file = open('input_task01.txt')
lst=file.read().split()
# print(lst)
a=[]
for i in lst[1:]:
    a+=[int(i)]
# print(a)
file.close()
sorted_list=bubbleSort(a)
file2 = open('output_task01.txt','w')
for i in sorted_list:
    file2.write(str(i)+' ')
file2.close()

'''The best case scenario is when the array is sorted. 
This is when the average time complexity will be order of n. As the variable 'if_sorted' becomes True
and the function returns the array without iterating again'''

