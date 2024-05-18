#!/usr/bin/env python
# coding: utf-8

# In[24]:


import math
from queue import PriorityQueue

def Dijkstra (graph,source):
    n=len(graph)
    visited = [False]*n
    dist = [-1]*n
    dist[source-1] = 0
    prev = [None]*n
    Queue = PriorityQueue()
    Queue.put((dist[source-1],source))
    while Queue.empty() is not True:
        u = Queue.get()[1]
        if visited[u-1]:
            continue
        visited[u-1] = True
        if graph[u] != None:
            for i in graph[u]:
                v = i[0]
                
                if dist[u] > i[1]:
                    alt = i[1]
                else:
                    alt = dist[u - 1] + i[1]
                if alt<dist[v-1]:
                    dist[v-1]=alt
                    prev[v-1]=u
                    Queue.put((dist[v-1],v))

    if len(prev) != 1:
        arr = dist[1:]
        arr.sort()
        x=arr[0]
        dist[-1]=x
        
        for p in arr:
            file2.write(str(p)+" ")
        file2.write("\n")
        
    else:
        file2.write(f"1 \n")
        

    
file = open("input5")
file_input = file.readlines()
file2 = open("output5","w")
sources=[]
lst = []
lst2 = []
test_cases = int(file_input[0])
for i in range(1,len(file_input)):
    temp = file_input[i].split()
    if len(temp) == 3:
        lst2+=[temp]
    elif len(temp)==2:
        lst+=[temp]
    elif len(temp)==1:
        sources+=[temp]


for i in lst:
    graph = {}
    x = int(sources.pop(0)[0])
    for j in range(int(i[1])):
        edges = []
        w = list(map(int,lst2.pop(0)))
        if w[0] in graph.keys():
            edges = graph[w[0]]
        edges.append(w[1:])
        graph[w[0]] = edges
    B = int(i[0])
    for v in range(1,(B+1)):
        if v not in graph:
            graph[v]=None
        
    graph={x: y for x, y in sorted(graph.items())}
    Dijkstra(graph,x)

file.close()
file2.close()


# In[ ]:




