# Task 6
file_in = open("input6.txt","r")
file_out = open("output6.txt","w")
R, H = [int(i) for i in file_in.readline().split(" ")]

# Initializing the grid
grid = [[] for i in range(R)]

# Inserting the input elements into the grid
for i in range(R):
    for j in file_in.readline().split()[0] :
        grid[i].append(j)

def floodFill(r,c,g):
    # Checking whether the rows or columns exceed boundaries or the grid has any "#"
    if c < 0 or r < 0 or r >= R or c >= H or grid[r][c] == "#":
        return 0

    if grid[r][c] == "D":
        diamond = 1
    else:
        diamond = 0

    grid[r][c] = "#"
    diamond += floodFill(r - 1, c, g) # Going Up
    diamond += floodFill(r + 1, c, g) # Going Down
    diamond += floodFill(r, c - 1, g) # Going Left
    diamond += floodFill(r, c + 1, g) # Going Right

    return diamond

max_diamond = 0 # Takes the count of maximum diamonds
for line in range(R):
    for char in range(H):
        if grid[line][char] == ".":
            # To count diamonds starting from the current cell
            diamonds = floodFill(line,char,grid)
            # Updating max_diamond with the maximum count of diamonds
            max_diamond = max(max_diamond,diamonds)

file_out.write(f'{max_diamond}')
file_out.close()


'''
Explanation:

The code uses a flood-fill algorithm to explore a 2D grid.
It represents a jungle with diamonds ('D') and obstacles ('#').
It finds the maximum number of diamonds that can be collected, by starting from each empty cell ('.') and avoiding obstacles ('#').
The algorithm utilizes the flood-fill approach to identify the optimal starting position for maximizing diamond collection.
'''