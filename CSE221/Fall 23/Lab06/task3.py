f = open("input3.txt", "r")
f1 = open("output3.txt", "w")

people, k = [int(i) for i in f.readline().split()]

lst = []
for i in range(k):
    a, b = [int(i) for i in f.readline().split()]
    lst.append((a, b))

size = [1] * (k + 2)
size[0] = 0
parent = []

for i in range((k + 2)):
    parent.append(i)

def findp(r):
    if r == parent[r]:
        return r
    parent[r] = findp(parent[r])
    return parent[r]

for i in range(len(lst)):
    first_person = lst[i][0]
    sec_person = lst[i][1]
    a = findp(first_person)
    b = findp(sec_person)

    if a != b:
        parent[b] = a
        total = size[a] + size[b]
        size[a] = total
        f1.write(f"{size[a]}\n")
    else:
        f1.write(f"{size[a]}\n")

f.close()
f1.close()


"""
Explanation:

First, I created a list where two people are in a tuple.
Then, assigned a size list which will give me the size of a friend circle.
Then, I used the findp() method to find the parent.
After calculating the new size, I updated it and printed it.
"""