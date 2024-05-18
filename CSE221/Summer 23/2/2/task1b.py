def add_find(N, S, arr):
    dic = {}
    for i in range(N):
        x = S - arr[i]
        if x in dic:
            return f"{dic[x]} {i+1}"
        dic[arr[i]] = i+1
    return "IMPOSSIBLE"

try:
    with open("input1b.txt", "r") as file:
        N, S = map(int, file.readline().split())
        arr = list(map(int, file.readline().split()))

    with open('output1b.txt', 'w') as file:
        idx = add_find(N, S, arr)
        file.write(idx)
            
except Exception:
  pass