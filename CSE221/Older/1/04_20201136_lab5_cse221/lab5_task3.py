#!/usr/bin/env python
# coding: utf-8

# In[26]:


#TASK_03
file=open('lab5_input3')
file2=open('lab5_output3','w')
lst=file.readlines()
arr= lst[1].split()
arr=list(map(int,arr))
s_arr= sorted(arr)
call_str=lst[2]
p_q=[]
idx=0
seq=[]
J_hrs=0
j_hrs=0
for c in call_str:
  if c=='J':
    p_q.append(s_arr[idx])
    seq.append(s_arr[idx])
    J_hrs+=s_arr[idx]
    idx+=1

  elif c=='j':
    v=p_q.pop()
    seq.append(v)
    j_hrs+=v
for i in seq:
  file2.write(str(i)+' ')
file2.write('\n')
file2.write(f'Jack will work for {J_hrs} hours\n')
file2.write(f'Jill will work for {j_hrs} hours')


file.close()
file2.close()


# In[ ]:




