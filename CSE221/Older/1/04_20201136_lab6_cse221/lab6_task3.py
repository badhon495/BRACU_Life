#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
input =open("input3.txt")
lst = input.read().split()
# print(lst)
e1= lst[0]
# print(e1)
e2 = lst[1]
# print(e2)
e3 = lst[2]
# print(e3)

def LCS(x,y,z):
  m = len(x)+1
#   print(m)
  n = len(y)+1
#   print(n)
  o = len(z)+1
#   print(o)
  c=np.zeros((m,n,o))
  #print(c)
  t=np.zeros((m,n,o))
  #print(t)
  for i in range(1,m):
      for j in range(1,n):
        for k in range(1,o):
          if x[i-1]==y[j-1] and x[i-1]==z[k-1]:
              c[i][j][k]=1+(c[i-1][j-1][k-1])
          else:
              max_n=max(c[i-1][j][k],c[i][j-1][k])
              max_n=max(max_n,c[i][j][k-1])
              c[i][j][k]=max_n

  return c
tab=LCS(e1,e2,e3)
# print(tab)
output = open("output3.txt","w")
print(str(int(tab[-1][-1][-1])))
output.write(str(int(tab[-1][-1][-1])))
input.close()


# In[ ]:




