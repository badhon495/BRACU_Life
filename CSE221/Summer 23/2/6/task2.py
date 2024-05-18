x= open("input2.txt", "r")
output_file= open("output2.txt","w")
array=list(map(int, x.readline().split()))
node=array[0]
edge=array[1]
graph1={}
for i in range(1, node+1):
  if i not in graph1:
    graph1[i]={}

for i in range(edge):
  array1=list(map(int,x.readline().split()))
  if array1[0] in graph1:
    graph1[array1[0]].update({array1[1]: array1[2]})

alice_st, bob_st= list(map(int, x.readline().split()))


def dijkstra(graph, start):
  minimum_distance={}
  unvisited = graph.copy()

  for i in unvisited:
    minimum_distance[i]= float('inf')
  minimum_distance[start]=0

  while unvisited:

    min_distance_node=None

    for j in unvisited:
      if min_distance_node is None:
        min_distance_node= j
      elif minimum_distance[j]< minimum_distance[min_distance_node]:
        min_distance_node= j
    
    adj_routes =graph[min_distance_node].items()

    for child, cost in adj_routes:

      if cost+ minimum_distance[min_distance_node] < minimum_distance[child]:
          minimum_distance[child]= cost+ minimum_distance[min_distance_node]

    unvisited.pop(min_distance_node)
  return minimum_distance

x=dijkstra(graph1, alice_st)
y=dijkstra(graph1, bob_st)

meeting= -1
shortest_distance=float('inf')
distance= None
alice=[]
bob=[]

for u,v in x.items():
  alice.append(v)
for u, v in y.items():
  bob.append(v)

for i in range(1, node):
  if alice[i] != float('inf') and bob[i] != float('inf'):
    distance =max(alice[i], bob[i])
    if distance< shortest_distance:
      shortest_distance= distance
      meeting= i+1

if distance == None:
  print("Impossible", file= output_file)
else:
  print("Time:", shortest_distance, file=output_file)
  print("Node:", meeting, file= output_file)

output_file.close()