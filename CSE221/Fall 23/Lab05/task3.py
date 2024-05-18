x = open("input3.txt", "r")
out_file = open("output3.txt", "w")
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

def strongly_connected(graph):
    def dfs(u, stack):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v, stack)
        stack.append(u)

    def dfs_reverse(u, component):
        visited[u] = True
        component.append(u)
        for v in transposed[u]:
            if not visited[v]:
                dfs_reverse(v, component)

    n = len(graph)
    visited = [False] * (n + 1)
    stack = []
    for u in graph:
        if not visited[u]:
            dfs(u, stack)

    transposed = {u: [] for u in graph}
    for u in graph:
        for v in graph[u]:
            transposed[v].append(u)

    visited = [False] * (n + 1)
    result = []
    while stack:
        u = stack.pop()
        if not visited[u]:
            component = []
            dfs_reverse(u, component)
            result.append(component)

    for i in sorted(result):
        for j in i:
            print(j, end=" ", file=out_file)
        print(file=out_file)

strongly_connected(graph1)