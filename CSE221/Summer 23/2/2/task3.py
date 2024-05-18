def merge(a, b):
    l = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            l.append(a[i])
            i += 1
        else:
            l.append(b[j])
            j += 1

    while i < len(a):
        l.append(a[i])
        i += 1

    while j < len(b):
        l.append(b[j])
        j += 1

    return l

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)

with open('input3.txt', 'r') as file:
    N = int(file.readline())
    n = list(map(int, file.readline().split()))

outp = mergeSort(n)

with open('output3.txt', 'w') as file:
    file.write(' '.join(map(str, outp)))