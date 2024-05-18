f=open("input3.txt","r")
f1=open("output3.txt","w")

dict1 = {}

a,b = [int(i) for i in f.readline().split()]

for i in range(a+1):
  dict1.update({i:[]})

for lines in f:
  l = lines.split()
  dict1[int(l[0])].append(int(l[1]))
  dict1[int(l[1])].append(int(l[0]))
#print(dict1)
output=[]
visited=[0]*(a+1)

def dfs(visited, graph, node):
  if visited[node]==0:
    output.append(node)
    visited[node]=1
    for neighbour in graph[node]:
      dfs(visited, graph, neighbour)
dfs(visited, dict1, 1)

for i in output:
  f1.write(str(i)+" ")
f.close()
f1.close()