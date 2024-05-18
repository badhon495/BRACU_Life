#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
file =open("input2.txt")
lst=file.read().split()
file.close()
zones={1:"Yasnaya",2:"Rozhok" ,3 :"School",4 :"Pochinki",5 :"Farm" ,6 :"Mylta",7 :"Shelter",8 :"Prison"}
zone=int(lst[0])
zone_seq=lst[1]
zone_pred=lst[2]
def CS(X, Y):
  m =len(X) + 1
  n =len(Y) + 1
  c=np.zeros((m,n))
  t=np.zeros((m,n))
  # c=[[0]*n]*m
  # t=[[0]*n]*m
  for x in range(len(t)):
        if x==0:
            for i in range (len(t[x])):
                t[x][i]=None
        else:
            t[x][0]=None

  for i in range(1,m):
        for j in range(1,n):
            if zone_seq[j-1]==zone_pred[i-1]:
                c[i][j]=((c[i-1][j-1])+1)
                t[i][j]="3"
            else:
                c[i][j]=max(c[i-1][j],c[i][j-1])
                if c[i][j]==c[i][j-1]:
                    t[i][j]="2"
                else: t[i][j]="1"

  return c 
tab=CS(zone_seq,zone_pred)

start=-1
result=""
for i in range (-1,-len(tab),-1):
    for j in range (start,-len(tab[i]),-1):
        if (tab[i][j-1]==tab[i-1][j]) and tab[i][j] !=tab[i][j-1] and tab[i][j] !=tab[i-1][j]:
            result=(zones[(j+8)+1])+" "+result
            start=j
            break
        if (tab[i][j-1]==tab[i-1][j]) and tab[i][j] ==tab[i][j-1] and tab[i][j] ==tab[i-1][j]:
            break 
correctness=(tab[-1][-1]/zone)*100
result+="\nCorrectness of prediction: "+str(int(correctness))+"%"
file2=open('output2.txt','w')
print(result)
file2.write(result)
file2.close()


# In[ ]:




