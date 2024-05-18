# Task 1a
file_in = 'input1a.txt'
with open(file_in, 'r') as file:
    lines = file.readlines()
    vertices, edges = lines[0].split(' ')
    #print(f"Vertices: {vertices}, Edges: {edges}")

graph_data = [tuple(map(int, i.strip().split())) for i in lines[1:]]
#print(graph_data)

def adjacencyMatrix(graph_data):
    adj_matrix = [[0 for i in range(int(vertices) + 1)] for j in range(int(vertices) + 1)]

    for i in graph_data:
        u, v, w = i
        adj_matrix[u][v] = w

    return adj_matrix    

result = adjacencyMatrix(graph_data)

file_out = 'output1a.txt'
with open(file_out, 'w') as file:
    for row in result:
        row_str = ' '.join(map(str, row))
        #print(row_str)
        file.write(row_str + '\n')  


'''
Explanation:

For creating an adjaceny matrix, I take a list, adj_mat.
In this list we have number of vertices + 1 indexes and in each indexes,
I created a list which have number of vertices + 1 indexes, and initially the values are 0.
Then from the inputs, I updated the values which indicate weights.
'''