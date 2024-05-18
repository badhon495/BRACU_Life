# Task 5
file_in = 'input5.txt'
with open(file_in, 'r') as file:
    lines = file.readlines()
    vertices, edges, destination = map(int, lines[0].split(' '))

edges = [tuple(map(int, i.strip().split())) for i in lines[1:]]

def adjacencyList(edges):
    adj_list = {}
    for edge in edges:
        u, v = edge
        adj_list.setdefault(u, []).append(v)
        adj_list.setdefault(v, []).append(u)  

    return adj_list

graph = adjacencyList(edges)

visited = [False for i in range(vertices + 1)]
distance = [float('inf') for i in range(vertices + 1)]
parent = [-1 for i in range(vertices + 1)]
result = []

def BFS(G, s):
    queue = [s]
    visited[s] = True
    distance[s] = 0
    while queue:
        u = queue.pop(0)
        #print(u, end=" ")
        result.append(u)
        for v in G[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u

BFS(graph, 1)

path = []
curr = destination
while curr != -1:
    path.append(curr)
    curr = parent[curr]
path.reverse()

time = distance[destination]
shortest_path = " ".join(map(str, path))

print("Time:", time)
print("Shortest Path:", shortest_path)

file_out = 'output5.txt'
with open(file_out, 'w') as file:
    file.write(f"Time: {time}\n")
    file.write(f"Shortest Path: {shortest_path}")


'''
Explanation:

In this task, I take a list which counts the distance where value is initially infinity.
This modified BFS algorithm keep track the distance, parent and children nodes.
Since, the graph is undirected and unweighted, and we know BFS uses level order traveral method,
Therefore, it will always give the shortest path.  
Everytime I enqueue the nodes, I update both the distance list.
'''