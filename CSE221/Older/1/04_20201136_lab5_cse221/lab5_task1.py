#!/usr/bin/env python
# coding: utf-8

# In[13]:


#TASK_01
file=open('lab5_input1')
file2=open('lab5_output1','w')
lst=file.readlines()
#lst=list(map(int,lst))
lst2=[]
for i in range(1,len(lst)):
  lst2.append(lst[i].split())

arr=[]
for i in range(len(lst2)):
  arr.append([int(lst2[i][0]),int(lst2[i][1])])

s_arr= sorted(arr, key=lambda x:x[1])

selected=[[s_arr[0][0],s_arr[0][1]]]
f=s_arr[0][1]
count=1
for c in range(len(arr)):
  if s_arr[c][0]>=f:
    count+=1
    f=s_arr[c][1]
    selected.append([s_arr[c][0],f])

# print(arr)
file2.write(str(count)+'\n')
for i in range(len(selected)):
  file2.write(str(selected[i][0])+','+str(selected[i][1]))
  file2.write('\n')
# print(selected)
file.close()
file2.close()


# In[ ]:




