def addition_finder(N, S, arr):
    
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] + arr[j] == S:
                return f"{i+1} {j+1}"
    return "IMPOSSIBLE"
try:
    with open('input1a.txt', 'r') as file:
        N, S = map(int, file.readline().split())
        arr = list(map(int, file.readline().split()))

    with open('output1a.txt', 'w') as file:
        idx = addition_finder(N, S, arr)
        file.write(idx)
            
except Exception:
  pass