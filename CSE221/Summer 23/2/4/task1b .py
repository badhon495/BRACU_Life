f=open("input1b.txt","r")
f1=open("output1b.txt","w")

r1=f.readline().split()
adj_lst=[[] for i in range(int(r1[0])+1)]
#print(adj_mat)
for lines in f:
  read=lines.split()
  adj_lst[int(read[0])].append((int(read[1]),int(read[2])))
#for i in range(len(adj_lst)):
  #f1.write(f"{i} : {adj_lst[i]}\n")

for i in range(len(adj_lst)):
  f1.write(f'{i} : ')
  for j in adj_lst[i]:
    f1.write(f"{j} ")
  f1.writelines('\n')
f.close()
f1.close()
print(adj_lst)