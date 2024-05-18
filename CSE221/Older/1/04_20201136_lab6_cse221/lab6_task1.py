#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=25
arr=[1000]*(n+1)
arr[0]=0

for i in range(1,n+1):
  for d in str(i):

    arr[i]=min(arr[i],arr[i-int(d)]+1)

print(arr[n])

