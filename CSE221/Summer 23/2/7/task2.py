f=open("Input2.txt","r")
f1=open("output2.txt","w")
task,people=[int(i) for i in f.readline().split()]
#print(people)
#print(task)
Q=[]
for line in f:
  start,end=[int(i) for i in line.split()]
  Q.append((start,end))

def gg(Q):
  return Q[1]
Q.sort(key=gg)
#print(Q)

def maxx(Q,people):
  count=0
  end_times=[-99999]*people
  for tup in Q:
    start,end=tup
    for j in range(people):
      if start>=end_times[j]:
        count+=1
        end_times[j]=end
        break

  return count

output=maxx(Q,people)
#print(output)
f1.write(f"{output}")

f.close()
f1.close()