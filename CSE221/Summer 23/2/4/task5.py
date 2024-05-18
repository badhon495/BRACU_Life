f=open("input5.txt","r")
f1=open("output5.txt","w")

read1=f.readline().split()
print(read1)
lst=[[0 for i in range(int(read1[0])+1)] for j in range(int(read1[0])+1)]
lst1 = [-1]*(int(read1[0])+1)
for lines in f:
  read=lines.split()
  lst[int(read[0])][int(read[1])]=1
  lst[int(read[1])][int(read[0])]=1

#print(lst)

def BFS(G,d,s):
  ancester=[0]*(int(read1[0])+1)
  out = []
  Q = []
  d[s] = 0
  Q.append(s)
  #print(Q)

  while Q != []:
    u = Q.pop(0)
    out.append(u)
    for v in range(len(G[u])):
      if G[u][v] != 0:
        if d[v] == -1:
          d[v] =d[u]+ 1
          ancester[v]=u
          Q.append(v)


  return (d,ancester)

out,ancester = BFS(lst,lst1,1)
Time=out[int(read1[2])]
#print(Time)
#print(ancester)
path=[]
path.append(int(read1[2]))
x=ancester[int(read1[2])]
path.append(x)
while ancester[x]!=0:
  x=ancester[x]
  path.append(x)
path.reverse()

f1.write(f"Time: {Time}\n")
f1.write(f"Shortest path: ")
for i in path:
  f1.write(str(i)+" ")
f.close()
f1.close()