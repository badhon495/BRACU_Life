x = open("input2.txt", "r")
out_file = open("output2.txt", "w")
arr = list(map(int, x.readline().split()))
node = arr[0]
edge = arr[1]

graph1 = {}
for i in range(1, node + 1):
    if i not in graph1:
        graph1[i] = []

for i in range(edge):
    array1 = list(map(int, x.readline().split()))
    if array1[0] in graph1:
        graph1[array1[0]].append(array1[1])

def bfs_topological(graph):
    in_degree = {node: 0 for node in graph}
    for i in graph.values():
        for j in i:
            in_degree[j] += 1

    queue = [node for node in in_degree if in_degree[node] == 0]
    result = []

    while queue:
        queue.sort()
        node = queue.pop(0)
        result.append(node)
        for j in graph[node]:
            in_degree[j] -= 1
            if in_degree[j] == 0:
                queue.append(j)

    if len(result) != len(graph):
        print("IMPOSSIBLE", file=out_file)
        return
    
    for i in result:
        print(i, end=" ", file=out_file)

bfs_topological(graph1)