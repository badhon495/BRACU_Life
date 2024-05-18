#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Task_04
import math
file=open('lab5_input4')
file2=open('lab5_output4','w')
lst=file.readlines()
for i in range(len(lst)):
  arr= lst[i].split()
  arr=list(map(int,arr))
  # print(arr)
  count=0
  if arr[0]==arr[1]==0:
    break
  for j in range(arr[0],arr[1]+1):
    root=math.sqrt(j)
    # print(root)
    if root==int(root):
      count+=1

  file2.write(str(count)+'\n')


# In[ ]:




