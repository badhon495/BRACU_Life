#!/usr/bin/env python
# coding: utf-8

# In[29]:


import heapq
import math
file = open("input4")
file2 = open("output4", "w")
lst = file.read().split("\n")
graph = {}
weight = {}
for x in lst:
    u,v,w=x.split(" ")
    if u not in graph.keys():
        graph[u]=[]
    graph[u]+=[v]
    weight[u,v]=int(w)
    if v not in graph.keys():
        graph[v]=[]

def Dijkstra(graph, s, d):
    visited = {}
    prev = {}
    dist = {}

    for i in graph.keys():
        dist[i]= math.inf
        visited[i]=False
    prev[s]=-1
    q=[]
    dist[s]=0
    heapq.heappush(q,(dist[s],s))

    while q!=[]:
        popped= heapq.heappop(q)
        if visited[popped[1]]:
            continue
        visited[popped[1]]=True
        for v in graph[popped[1]]:
            alt = dist[popped[1]]+weight[(popped[1],v)]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = popped[1]
                heapq.heappush(q, (dist[v], v))
    x = str(d)
    p=d
    while p!=-1:
        p = prev[p]
        if p!=-1:
            x = str(p)+" "+x
    return x

route = Dijkstra(graph, 'Motijheel',"MOGHBAZAR")
file2.write(route)

file.close()
file2.close()


# In[ ]:




