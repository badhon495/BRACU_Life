# Task 1b
file_in = 'input1b.txt'
with open(file_in, 'r') as file:
    lines = file.readlines()
    vertices, edges = lines[0].split(' ')
    #print(f"Vertices: {vertices}, Edges: {edges}")

graph_data = [tuple(map(int, i.strip().split())) for i in lines[1:]]
#print(graph_data)

def adjacencyList(graph_data):
    adj_list = [[] for i in range(int(vertices) + 1)]

    for i in graph_data:
        u, v, w = i
        adj_list[u].append((v, w))

    return adj_list  

result = adjacencyList(graph_data)

file_out = 'output1b.txt'
with open(file_out, 'w') as file:
    for i in range(len(result)):
        #print(f"{i} : {result[i]}")
        edge_str = ' '.join(f"({v}, {w})" for v, w in result[i])
        file.write(f"{i} : {edge_str}")
        file.writelines('\n')


'''
Explanation:

For creating an adjacency list, I take a list, adj_list.
In this list we have number of vertices + 1 index, and in each index I created an empty list.
In the empty list, I stored the connected nodes and weight in a tuple.  
'''