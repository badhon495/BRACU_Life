#!/usr/bin/env python
# coding: utf-8

# In[20]:


#TASK_02
file=open('lab5_input2')
file2=open('lab5_output2','w')
lst=file.readlines()
#lst=list(map(int,lst))
lst2=[]
for i in range(len(lst)):
  lst2.append(lst[i].split())

arr=[]
for i in range(len(lst2)):
  arr.append([int(lst2[i][0]),int(lst2[i][1])])

s_arr= sorted(arr[1:], key=lambda x:x[1])

n= arr[0][0]
m= arr[0][1]
f=[0]*m

for i in range(m):
  f[i]=s_arr[i][1]

count= m


# selected=[[s_arr[0][0],s_arr[0][1]]]
# f=s_arr[0][1]
# count=1
for c in range(m,n):
  for i in range(m):
    if s_arr[c][0]>=f[i]:
      count+=1
      f[i]=s_arr[c][1]
      break
    # selected.append([s_arr[c][0],f])

# print(arr)
# print(s_arr)
# print(f)
file2.write(str(count))
# print(selected)
file.close()


# In[ ]:




