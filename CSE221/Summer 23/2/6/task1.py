x= open("input1.txt", "r")
out_file= open("output1.txt","w")
arr=list(map(int, x.readline().split()))
node=arr[0]
edge=arr[1]

graph1={}
for i in range(1, edge):
  if i not in graph1:
    graph1[i]={}

for i in range(edge):
  array1=list(map(int,x.readline().split()))
  if array1[0] in graph1:
    graph1[array1[0]].update({array1[1]: array1[2]})


source=x.readline().strip()

def dijkstra(graph, start, destination):
  d={}
  unvisited_graph = graph.copy()
  
  for i in unvisited_graph:
    d[i]= float('inf')
  d[start]=0

  while unvisited_graph:

    d_node=None

    for j in unvisited_graph:
      if d_node is None:
        d_node= j
      elif d[j]< d[d_node]:
        d_node= j
    
    adj_routes =graph[d_node].items()

    for child, cost in adj_routes:

      if cost+ d[d_node] < d[child]:
          d[child]= cost+ d[d_node]

    unvisited_graph.pop(d_node)

  if d[destination]!=float('inf'):
    print(f'{d[destination]} ', end="", file=out_file)

  else:
    print("-1 ", end="", file=out_file) 


for i in range(1,node+1):
  dijkstra(graph1, int(source), i)


out_file.close()     