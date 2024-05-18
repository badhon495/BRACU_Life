f=open("input1a.txt","r")
f1=open("output1a.txt","w")

r1=f.readline().split()
adj_mat=[[0 for i in range(int(r1[0])+1)] for j in range(int(r1[0])+1)]
#print(adj_mat)
for lines in f:
  read=lines.split()
  adj_mat[int(read[0])][int(read[1])]=int(read[2])
for i in adj_mat:
  for j in i:
    f1.writelines(str(j)+" ")
  f1.writelines('\n')
f.close()
f1.close()
print(adj_mat)