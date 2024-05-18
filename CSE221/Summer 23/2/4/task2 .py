f=open("input2.txt","r")
f1=open("output2.txt","w")

read1=f.readline().split()
#print(read1)
lst=[[0 for i in range(int(read1[0])+1)] for j in range(int(read1[0])+1)]
lst1 = [0]*(int(read1[0])+1)
for lines in f:
  read=lines.split()
  lst[int(read[0])][int(read[1])]=1
  lst[int(read[1])][int(read[0])]=1

#print(lst)

def BFS(G,G1,s):
  out = []
  Q = []
  G1[s] = 1
  Q.append(s)
  print(Q)

  while Q != []:
    u = Q.pop(0)
    out.append(u)
    for v in range(len(G[u])):
      if G[u][v] != 0:
        if G1[v] == 0:
          G1[v] = 1
          Q.append(v)


  return out

out = BFS(lst,lst1,1)

for i in out:
  f1.write(str(i)+" ")
f.close()
f1.close()

