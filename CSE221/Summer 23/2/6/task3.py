x= open("input3.txt", "r")
array=list(map(int, x.readline().split()))
output_file= open("output3.txt","w")
node=array[0]
edge=array[1]
infinity= float('inf')
graph1={}
for i in range(1, node+1):
  if i not in graph1:
    graph1[i]={}

for i in range(edge):
  array1=list(map(int,x.readline().split()))
  if array1[0] in graph1:
    graph1[array1[0]].update({array1[1]: array1[2]})


def dijkstra(graph, start, destination):
  minimum_distance={}
  unvisited = graph.copy()
  infinity= float('inf')
  track_predecessor={}
  track_path=[]
  edges={}

  for i in unvisited:
    minimum_distance[i]= infinity
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
        
      if minimum_distance[min_distance_node] < minimum_distance[child]:
          minimum_distance[child]= cost
          track_predecessor[child]= min_distance_node
          edges[min_distance_node]= cost       

    unvisited.pop(min_distance_node)

  currentNode=destination

  while currentNode!=start:
    try:
      track_path.insert(0, currentNode)
      currentNode =track_predecessor[currentNode]
    except KeyError:
      print("Impossible",file=output_file)
      return
  track_path.insert(0, start)

  danger=[]
  for i in track_path:
    danger.append(minimum_distance[i])
  print(max(danger), file= output_file)


dijkstra(graph1, 1, int(node))

output_file.close()