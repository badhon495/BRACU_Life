# Task 3
file_in = 'input3.txt'
with open(file_in, 'r') as file:
    lines = file.readlines()
    vertices, edges = lines[0].split(' ')    
    #print(f"Vertices: {vertices}, Edges: {edges}")    

edges = [tuple(map(int, i.strip().split())) for i in lines[1:]]
#print(edges)

def adjacencyList(edges):
    adj_list = {}
    for edge in edges:
        u, v = edge
        adj_list.setdefault(u, []).append(v)
        adj_list.setdefault(v, []).append(u)

    #print(adj_list)
    return adj_list

graph = adjacencyList(edges)
visited = [False for i in range(int(vertices) + 1)]
result = []

def DFS(G, u):
    visited[u] = True
    #print(u, end=" ")
    result.append(u) 
    for v in G[u]:
        if not visited[v]:
            DFS(G, v)   

DFS(graph, 1)

file_out = 'output3.txt'
with open(file_out, 'w') as file:
    for i in result:
        file.write(str(i) + " ")


'''
Explanation:

Here, I represented the graph in a dictionary.
I take a boolean visited list which keeps track of whether the nodes are visited or not, and initially the value is False.
In the DFS() method if the node is not visited, then I append the node in the result and update it in the visited list.
And, for every neighbor I call the same DFS() method recursively. 
'''