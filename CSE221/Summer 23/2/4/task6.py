f=open('input6.txt','r')
f1=open('output6.txt','w')
lst=f.readline()
lst=lst.split()
row=int(lst[0])
column=int(lst[1])
G=[]
for i in range(row):
    G.append([])

c=0
while c<row:
  line=f.readline()
  line=line.split()
  for i in line:
    for j in range(len(i)):
      G[c].append(i[j])
  c+=1
print(G)
def valid(x, y, R, H):
    return 0 <= x < R and 0 <= y < H

def floodFill(grid, x, y, visited):
  if not valid(x, y, len(grid), len(grid[0])) or grid[x][y] == '#' or visited[x][y]:
    return 0

  visited[x][y] = True
  diamonds = 0

  if grid[x][y] == 'D':
    diamonds = 1

  for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    diamonds += floodFill(grid, x + a, y + b, visited)
  return diamonds

def findMax(grid):
  R,H = len(grid), len(grid[0])
  maxDiamonds = 0

  for x in range(R):
    for y in range(H):
      if grid[x][y] == '.':
        visited = [[False for _ in range(H)] for _ in range(R)]
        maxDiamonds = max(maxDiamonds, floodFill(grid, x, y, visited))

  return maxDiamonds

out=findMax(G)
#print(out)
f1.write(f"{out}")
f.close()
f1.close()