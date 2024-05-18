f=open("Input3.txt","r")
f1=open("output3.txt","w")

people,k=[int(i) for i in f.readline().split()]

lst=[]
for i in range(k):
  a,b=[int(i) for i in f.readline().split()]
  lst.append((a,b))
#print(lst)

size = [1]*(k+2)
size[0] = 0
parent =[]
for i in range((k+2)) :
  parent.append(i)

#print(parent)

def findp(r):
  if(r==parent[r]):
    return r
  parent[r]=findp(parent[r])
  return parent[r]

for i in range(len(lst)):
  first_person=lst[i][0]
  sec_person=lst[i][1]
  a= findp(first_person)
  b=findp(sec_person)

  if(a!=b):
    parent[b]=a
    total=size[a]+size[b]
    size[a]=total
    f1.write(f"{size[a]}\n")
  else:
    f1.write(f"{size[a]}\n")

f.close()
f1.close()