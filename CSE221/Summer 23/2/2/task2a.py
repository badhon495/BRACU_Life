def func(list1, list2):
    l = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            l.append(list1[i])
            i += 1
        else:
            l.append(list2[j])
            j += 1
    l.extend(list1[i:])
    l.extend(list2[j:])
    return l

with open('input2a.txt', 'r') as file:
    N = int(file.readline())
    alice = list(map(int, file.readline().split()))
    M = int(file.readline())
    bob = list(map(int, file.readline().split()))

out = func(alice, bob)

with open('output2a.txt', 'w') as file:
    file.write(' '.join(map(str, out)))