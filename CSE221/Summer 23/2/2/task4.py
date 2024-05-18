def max_n(arr, s, e):
    if s == e:
        return arr[s]

    mid = (s + e) // 2
    max_l = max_n(arr, s, mid)
    max_r = max_n(arr, mid + 1, e)

    return max(max_l, max_r)

with open("input4.txt", "r") as file:
    N = int(file.readline())
    arr = list(map(int, file.readline().split()))

maxValue = max_n(arr, 0, N - 1)

with open("output4.txt", "w") as file:
    file.write(str(maxValue))