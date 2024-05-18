def func(list1, list2):
    l = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            l.append(list1[i])
            i += 1
        else:
            l.append(list2[j])
            j += 1

    while i < len(list1):
        l.append(list1[i])
        i += 1

    while j < len(list2):
        l.append(list2[j])
        j += 1

    return l

with open('input2b.txt', 'r') as file:
    N = int(file.readline())
    list1 = list(map(int, file.readline().split()))
    M = int(file.readline())
    list2 = list(map(int, file.readline().split()))

out = func(list1, list2)

with open('output2b.txt', 'w') as file:
    file.write(' '.join(map(str, out)))