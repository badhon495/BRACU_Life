# Task 4
file_in = 'input4.txt'
with open(file_in, 'r') as file:
    lines = file.readlines()
    vertices, edges = map(int, lines[0].split(' '))

edges = [tuple(map(int, i.strip().split())) for i in lines[1:]]

def adjacencyList(edges):
    adj_list = {}
    for edge in edges:
        u, v = edge
        adj_list.setdefault(u, []).append(v)

    return adj_list

adj_list = adjacencyList(edges)

order = []
def topologicalSort():
    indegree = {v: 0 for v in range(1, vertices + 1)}
    #print(indegree)

    for neighbors in adj_list.values():
        for neighbor in neighbors:
            indegree[neighbor] += 1

    Queue = [v for v, degree in indegree.items() if degree == 0]
    #print(Queue)

    while Queue:
        u = Queue.pop(0)
        #print(u, end=" ")
        order.append(u)
        for v in adj_list.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0:
                Queue.append(v)

topologicalSort()

file_out = 'output4.txt'
with open(file_out, 'w') as file:
    if len(order) == vertices:
        file.write("NO")
    else:
        file.write("YES")


'''
Explanation:

In this task, I use topological sorting algorithm, which is Kahn's algorithm.
Since, we know, topological sort only possible in DAG.
Thus, after the sorting, if the sorted list length == number of vertex, then there is no cycle.
Otherwise, there is a cycle.
I created an indegree dictionary and modified the BFS algorithm.  
'''