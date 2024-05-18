f=open("input1.txt","r")
f1=open("output1.txt","w")
task=f.readline()
#print(task)
Q=[]
for line in f:
  start,end=[int(i) for i in line.split()]
  Q.append((start,end))

def gg(Q):
  return Q[1]
Q.sort(key=gg)
#print(Q)

result=[]
u=Q.pop(0)
result.append(u)
temp=u[1]
#print(temp)
count=1
while Q!=[]:
  tup=Q.pop(0)
  if(tup[0]>=temp):
    result.append(tup)
    temp=tup[1]
    count+=1

#print(count)
#print(result)

f1.write(f"{count}\n")
for i in result:
  f1.write(f"{i[0]} {i[1]}\n")

f.close()
f1.close()