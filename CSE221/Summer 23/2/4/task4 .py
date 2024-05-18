
f=open("input4.txt",'r')
f1=open("output4.txt",'w')
read1=f.readline().split()

lst=[[0 for i in range(int(read1[0])+1)] for j in range(int(read1[0])+1)]
lst1 = [0]*(int(read1[0])+1)

for lines in f:
  read=lines.split()
  lst[int(read[0])][int(read[1])]=1

#print(read1)
order=[]

def topologicalSort():
  indegree = [0]*(int(read1[0])+1)
  for i in range(len(lst)):
    for j in range(len(lst[i])):
      if lst[i][j]==1:
        indegree[j] += 1

  #print(indegree)
  Q=[]

  for i in range(1,len(indegree)):
    if(indegree[i]==0):
      Q.append(i)
  #print(Q)

  while Q!=[]:
    u=Q.pop(0)
    order.append(u)

    for v in range(len(lst[u])):
      if(lst[u][v]==1):
        indegree[v]-=1

        if(indegree[v]==0):
          Q.append(v)

topologicalSort()
if(len(order)==int(read1[0])):
  f1.write(f"No")
else:
  f1.write("Yes")

f.close()
f1.close()