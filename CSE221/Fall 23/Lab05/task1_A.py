x = open("input1_A.txt", "r")
out_file = open("output1_A.txt", "w")
arr = list(map(int, x.readline().split()))
node = arr[0]
edge = arr[1]

graph1 = {}
has_pre = set()

for i in range(1, node + 1):
    if i not in graph1:
        graph1[i] = []

for i in range(edge):
    array1 = list(map(int, x.readline().split()))
    if array1[0] in graph1:
        has_pre.add(array1[1])
        graph1[array1[0]].append(array1[1])

def topological_sort(graph, start_node):
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        result.append(node)

    visited = {node: False for node in graph}
    result = []
    for i in start_node:
        dfs(i)

    for node in graph:
        if not visited[node]:
            for adj in graph[node]:
                if visited[adj]:
                    print("IMPOSSIBLE", file=out_file)
                    return
            dfs(node)
    result.reverse()
    for i in result:
        print(i, end=" ", file=out_file)

all_nodes = list(set(graph1.keys()).difference(has_pre))
topological_sort(graph1, all_nodes)